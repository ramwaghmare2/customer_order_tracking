# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.order import Myorder
from .customer import Customer

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
