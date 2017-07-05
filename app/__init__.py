from flask import Flask

def create_app(config_name):
    global app 
    app = Flask(__name__, static_url_path='')
    app.config["SECRET_KEY"] = "KeepThisS3cr3t"
    from .log import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/log')
    return app
