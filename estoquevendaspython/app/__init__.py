"""Inicializa Flask, DB e JWT."""
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    jwt.init_app(app) # Inicializa o JWT
    
    return app