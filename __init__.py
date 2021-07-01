from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

db = SQLAlchemy()

DB_NAME = "activity_db.db"




def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    # initialize the database
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # register blueprints
    from .views import views

    app.register_blueprint(views, prefix="")

    return app


# def create_db(app):
#     if not os.path.exists(f"base/{DB_NAME}"):
#         db.create_all(app=app)
#         print("Database has been created")
