from werkzeug.security import generate_password_hash
from app.models import db, Usuario
from app import create_app

app = create_app()
with app.app_context():
    admin = Usuario(
        nome="Admin Sistema",
        login="admin",
        senha=generate_password_hash("admin123"),
        perfil="admin"
    )
    db.session.add(admin)
    db.session.commit()
    print("Usuário Admin criado com sucesso!")