from flask import Flask
from austinbush.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from austinbush.main.routes import main
    from austinbush.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app