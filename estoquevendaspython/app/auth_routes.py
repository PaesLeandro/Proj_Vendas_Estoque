"""Rotas de autenticação e proteção JWT."""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from .models import Usuario, db
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(login=data.get('login')).first()
    
    if usuario and check_password_hash(usuario.senha, data.get('senha')):
        # O "claims" permite embutir o perfil do usuário no token
        access_token = create_access_token(
            identity=usuario.login, 
            additional_claims={"perfil": usuario.perfil}
        )
        return jsonify(access_token=access_token), 200
    
    return jsonify({"erro": "Credenciais inválidas"}), 401

# Exemplo de rota protegida apenas para ADMIN
@auth.route('/admin/dashboard', methods=['GET'])
@jwt_required()
def dashboard_admin():
    claims = get_jwt()
    if claims.get("perfil") != 'admin':
        return jsonify({"erro": "Acesso negado. Apenas administradores."}), 403
        
    return jsonify({"mensagem": "Bem-vindo ao painel administrativo!"})