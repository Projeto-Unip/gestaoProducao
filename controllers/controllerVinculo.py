from flask import Blueprint, jsonify, request
from models.fornecedor import fornecedor
from models.materialPrima import materia_prima
from database.dba import db

vinculo_db = Blueprint('vinculo', __name__, url_prefix="/api")

@vinculo_db.route("/vincularMaterial", methods=["POST"])
def vincularMaterial():
    try:
        dados = request.json
        
        if not dados or 'id_fornecedor' not in dados or 'id_materiaPrima' not in dados:
            return jsonify({"erro": "Dados incompletos. Envie id_fornecedor e id_materiaPrima"}), 400
        
        forn = db.session.get(fornecedor, dados['id_fornecedor'])
        material = db.session.get(materia_prima, dados['id_materiaPrima'])
        
        if not fornecedor:
            return jsonify({"erro": f"Fornecedor com ID {dados['id_fornecedor']} não encontrado."}), 404
        
        if not material:
            return jsonify({"erro": f"Material com ID {dados['id_materiaPrima']} não encontrado."}), 404
        
        if material in fornecedor.materiais:
            return jsonify({"mensagem": "Vínculo já existe!"}), 200
        
        fornecedor.materiais.append(material)
        db.session.commit()
        
        return jsonify({"mensagem": f"Material '{material.nome}' vinculado ao fornecedor '{fornecedor.razao_social}' com sucesso."}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@vinculo_db.route("/desvincularMaterial", methods=["DELETE"])
def desvincularMaterial():
    try:
        dados = request.json
        
        if not dados or 'id_fornecedor' not in dados or 'id_materiaPrima' not in dados:
            return jsonify({"erro": "Dados incompletos. Envie id_fornecedor e id_materiaPrima"}), 400
        
        forn = db.session.get(fornecedor, dados['id_fornecedor'])
        material = db.session.get(materia_prima, dados['id_materiaPrima'])
        
        if not fornecedor:
            return jsonify({"erro": f"Fornecedor com ID {dados['id_fornecedor']} não encontrado."}), 404
        
        if not material:
            return jsonify({"erro": f"Material com ID {dados['id_materiaPrima']} não encontrado."}), 404
        
        if material not in fornecedor.materiais:
            return jsonify({"erro": "Vínculo não existe!"}), 404
        
        fornecedor.materiais.remove(material)
        db.session.commit()
        
        return jsonify({"mensagem": f"Material '{material.nome}' desvinculado do fornecedor '{fornecedor.razao_social}' com sucesso."}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@vinculo_db.route("/fornecedor/<int:idFornecedor>/materiais", methods=["GET"])
def listarMateriaisFornecedor(idFornecedor):
    try:
        forn = db.session.get(fornecedor, idFornecedor)
        
        if not fornecedor:
            return jsonify({"erro": f"Fornecedor com ID {idFornecedor} não encontrado."}), 404
        
        materiais = [m.to_disc() for m in fornecedor.materiais]
        return jsonify({
            "fornecedor": fornecedor.razao_social,
            "materiais": materiais
        }), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@vinculo_db.route("/material/<int:idMaterial>/fornecedores", methods=["GET"])
def listarFornecedoresMaterial(idMaterial):
    try:
        material = db.session.get(materia_prima, idMaterial)
        
        if not material:
            return jsonify({"erro": f"Material com ID {idMaterial} não encontrado."}), 404
        
        fornecedores = [f.to_disc() for f in material.fornecedores]
        return jsonify({
            "material": material.nome,
            "fornecedores": fornecedores
        }), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
