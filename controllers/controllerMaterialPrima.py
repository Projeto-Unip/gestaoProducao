from flask import Blueprint, jsonify, request
from models.materialPrima import materia_prima
from database.dba import db

materialPrima_db = Blueprint('materia_prima', __name__, url_prefix="/api/materia-prima" )

@materialPrima_db.route("/", methods=["GET"])
def listar():
    try:
        stmt = db.select(materia_prima)
        materias = db.session.execute(stmt).scalars().all()
        
        materiaPrima_list = [m.to_disc() for m in materias]
        return jsonify(materiaPrima_list), 200
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return jsonify({"erro": "Ocorreu um erro ao buscar usuários"}), 500