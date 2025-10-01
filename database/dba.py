from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote # Importe esta função
import os
db = SQLAlchemy()

def init_app(app):
   # No seu arquivo app.py ou dba.py
    db_password = os.getenv('DB_PASSWORD')
    encoded_password = quote(db_password, safe='')

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{encoded_password}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)