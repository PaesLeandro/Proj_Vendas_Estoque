"""Configurações de banco e chaves."""
import os

class Config:
    # Caso não encontre a variável (rodando local sem docker), usa SQLite como fallback
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///estoque.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sua_chave_secreta_aqui'