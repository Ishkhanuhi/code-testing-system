import os

from flask import Flask


def create_app():
    database_uri = '{dialect}://{username}:{password}@{host}:{port}/{database}'.format(
        dialect=os.getenv('DB_DIALECT'),
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
    )

    app = Flask(__name__, template_folder='../../templates')
    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    return app


def register_extensions(app):
    from src.flask_app.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db, directory='src/database/migrations')


def register_blueprints(app):
    from src.flask_app.routes import blueprint

    app.register_blueprint(blueprint)
