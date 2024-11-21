from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilitar CORS para todas las rutas

    app.config['JWT_SECRET_KEY'] = 'your_secret_key'

    jwt = JWTManager(app)

    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .routes import sites_bp
    app.register_blueprint(sites_bp, url_prefix='/sites')

    return app