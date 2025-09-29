from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import urllib
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

driver = os.getenv("DB_DRIVER")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

params = urllib.parse.quote_plus(
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
)

connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

db = SQLAlchemy()
