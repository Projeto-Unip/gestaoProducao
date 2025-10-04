from flask import Flask
from controllers.controllerMaterialPrima import materiaPrima_db
from database.dba import init_app
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
init_app(app)
app.register_blueprint(materiaPrima_db)


if __name__ == "__main__":
    app.run(debug=True)
