"""Geração de relatórios e análises com pandas."""

import pandas as pd
from app.models import ItemVenda, Produto, Venda


def relatorio_faturamento_diario():
    # Consulta via SQLAlchemy e conversão para DataFrame
    query = Venda.query.all()
    data = [{'data': v.data.date(), 'valor': v.valor_total} for v in query]

    df = pd.DataFrame(data)
    if df.empty:
        return "Nenhuma venda registrada."

    # Agrupamento por data
    faturamento = df.groupby('data')['valor'].sum().reset_index()
    return faturamento


def get_produtos_mais_vendidos():
    itens = ItemVenda.query.all()
    data = [{"nome": i.venda.cliente.nome, "produto": i.produto_id,
             "qtd": i.quantidade} for i in itens]
    df = pd.DataFrame(data)

    if df.empty:
        return {}

    ranking = df.groupby('produto')['qtd'].sum().sort_values(ascending=False)
    return ranking.to_dict()


def get_estoque_critico(limite=5):
    produtos = Produto.query.filter(Produto.quantidade <= limite).all()
    return [{"nome": p.nome, "quantidade": p.quantidade} for p in produtos]
