"""Configurações de banco e chaves."""
import os


class Config:
    # Caso não encontre a variável (rodando local sem docker), usa SQLite como fallback
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///estoque.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get(
        'SECRET_KEY', 'troque_esta_chave_local_super_secreta_2026_mais_de_32_bytes')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', SECRET_KEY)
