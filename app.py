import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from sqlalchemy import MetaData
from config import config

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()


def register_extensions(app):

    db.init_app(app)
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from models import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    with app.app_context():
        register_extensions(app)

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app


if __name__ == "__main__":

    app = create_app(config_name=os.getenv("FLASK_ENV", "default"))
    app.run()
