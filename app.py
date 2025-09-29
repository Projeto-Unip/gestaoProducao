from flask import Flask
from routes.routersMateriaPrima import materia_prima_routes
from dba.database import db, connection_string

# Configurar conexão
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar banco
db.init_app(app)

app = Flask(__name__)
app.register_blueprint(materia_prima_routes)

if __name__ == "__main__":
    app.run(debug=True)
