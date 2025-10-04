from flask import Flask
from controllers.controllerMaterialPrima import materiaPrima_db
from controllers.controllerFornecedor import fornecedor_db
from controllers.controllerVinculo import vinculo_db
from controllers.controllerEtapaPesquisa import etapaPesquisa_db
from controllers.controllerStatusProducao import statusProducao_db
from controllers.controllerPesquisa import pesquisa_db
from controllers.controllerProducao import producao_db
from database.dba import init_app
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
init_app(app)

app.register_blueprint(materiaPrima_db)
app.register_blueprint(fornecedor_db)
app.register_blueprint(vinculo_db)
app.register_blueprint(etapaPesquisa_db)
app.register_blueprint(statusProducao_db)
app.register_blueprint(pesquisa_db)
app.register_blueprint(producao_db)


if __name__ == "__main__":
    app.run(debug=False)
