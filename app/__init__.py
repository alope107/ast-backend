from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    from .routes import parse_bp
    app.register_blueprint(parse_bp)

    return app