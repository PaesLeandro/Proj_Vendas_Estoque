"""Inicializa Flask, DB e JWT."""
from flask import Flask
from flask_jwt_extended import JWTManager
from .auth_routes import auth
from .models import db
from .routes import report_routes, routes

jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(routes)
    app.register_blueprint(report_routes)

    return app
