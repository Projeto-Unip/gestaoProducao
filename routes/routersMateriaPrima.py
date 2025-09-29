from flask import Blueprint, request, jsonify
from controllers.controllerMaterialPrima import criar_medicamento, obter_medicamentos, obter_medicamento, deletar_medicamento

materia_prima_routes = Blueprint("routersMateriaPrima", __name__)

@materia_prima_routes.route("/medicamentos", methods=["GET"])
def listar():
    return jsonify(obter_medicamentos())

@materia_prima_routes.route("/medicamentos", methods=["POST"])
def criar():
    data = request.json
    novo = criar_medicamento(data)
    return jsonify(novo), 201

@materia_prima_routes.route("/medicamentos/<int:id>", methods=["GET"])
def buscar(id):
    med = obter_medicamento(id)
    if med:
        return jsonify(med)
    return jsonify({"erro": "Medicamento não encontrado"}), 404

@materia_prima_routes.route("/medicamentos/<int:id>", methods=["DELETE"])
def remover(id):
    return jsonify(deletar_medicamento(id))
