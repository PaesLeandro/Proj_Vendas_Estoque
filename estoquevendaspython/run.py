"""Ponto de entrada da aplicação."""
from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    # Cria as tabelas se elas não existirem
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)