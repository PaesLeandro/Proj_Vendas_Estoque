from flask import Blueprint, request, jsonify
from .models import db, Produto, Venda, ItemVenda, Cliente
from flask_jwt_extended import jwt_required, get_jwt
import pandas as pd

routes = Blueprint('routes', __name__)
report_routes = Blueprint('reports', __name__)


@routes.route('/registrar_venda', methods=['POST'])
def registrar_venda():
    data = request.json
    cliente_id = data.get('cliente_id')
    # Lista de {'produto_id': 1, 'quantidade': 2}
    itens_comprados = data.get('itens')

    nova_venda = Venda(cliente_id=cliente_id, valor_total=0)
    total_geral = 0

    try:
        for item in itens_comprados:
            prod = Produto.query.get(item['produto_id'])

            # Validação de Estoque
            if prod.quantidade < item['quantidade']:
                return jsonify({"erro": f"Estoque insuficiente para {prod.nome}"}), 400

            # Cálculo de Subtotal
            subtotal = prod.preco * item['quantidade']
            total_geral += subtotal

            # Atualização de Estoque Automática
            prod.quantidade -= item['quantidade']

            # Criar Item da Venda
            item_venda = ItemVenda(
                produto_id=prod.id,
                quantidade=item['quantidade'],
                subtotal=subtotal
            )
            nova_venda.itens.append(item_venda)

        nova_venda.valor_total = total_geral
        db.session.add(nova_venda)
        db.session.commit()

        return jsonify({"mensagem": "Venda realizada com sucesso!", "venda_id": nova_venda.id}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@routes.route('/produtos', methods=['POST'])
@jwt_required()
def cadastrar_produto():
    claims = get_jwt()
    if claims.get("perfil") != 'admin':
        return jsonify({"erro": "Apenas administradores podem cadastrar produtos"}), 403

    data = request.json
    novo_p = Produto(
        nome=data['nome'],
        preco=data['preco'],
        categoria=data['categoria'],
        quantidade=data['quantidade']
    )
    db.session.add(novo_p)
    db.session.commit()
    return jsonify({"msg": "Produto cadastrado"}), 201


@report_routes.route('/relatorio/faturamento', methods=['GET'])
def faturamento_grafico():
    vendas = Venda.query.all()
    if not vendas:
        return jsonify([])

    data = [{"data": v.data.strftime(
        '%d/%m'), "valor": v.valor_total} for v in vendas]
    df = pd.DataFrame(data)

    faturamento_diario = df.groupby('data')['valor'].sum().reset_index()

    return jsonify(faturamento_diario.to_dict(orient='records'))
