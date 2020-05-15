from flask import Flask 

from .commands import create_tables

from .routes.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)


    app.register_blueprint(main)

    app.cli.add_command(create_tables)

    return app