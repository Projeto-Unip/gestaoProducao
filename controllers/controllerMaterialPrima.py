from flask import Blueprint, jsonify, request
from models.materialPrima import materia_prima
from database.dba import db
from datetime import datetime

materiaPrima_db = Blueprint('materia_prima', __name__, url_prefix="/api" )

@materiaPrima_db.route("/materia-prima", methods=["GET"])
def listar():
    try:
        stmt = db.select(materia_prima)
        materias = db.session.execute(stmt).scalars().all()
        
        materia_prima_list = [m.to_disc() for m in materias]
        return jsonify(materia_prima_list), 200
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return jsonify({"erro": "Ocorreu um erro ao buscar matérias-primas"}), 500


@materiaPrima_db.route("/addMateriaPrima", methods=["POST"])   
def addMateria():
   try:
        materiaPrima = request.json
        
        if not materiaPrima:
            return "Não foi possível identificar os dados enviados", 400
        
        # Verificando se o materia existe no dba
        nome_normalizado = materiaPrima.get('nome').strip().lower()
        smtp = db.select(materia_prima).where(materia_prima.nome == nome_normalizado)
        existMatPrima = db.session.execute(smtp).scalars().first()
        print(existMatPrima)
        
        if(not existMatPrima):
            addMateriaPrima = materia_prima(
            nome=nome_normalizado,
            formula=materiaPrima.get('formula'),
            qtd=materiaPrima.get('quantidade'),
            lote=materiaPrima.get('lote'),
            data_validade=materiaPrima.get('data_validade')
                )
            
            db.session.add(addMateriaPrima)
            db.session.commit()

            return jsonify(addMateriaPrima.to_disc()), 201
        else:
            return jsonify({"mensagem": "Materia prima existente!"}), 200

   except Exception as e:
       db.session.rollback() 
       return jsonify(f"Erro: {str(e)}"), 500
   

@materiaPrima_db.route('/updateMateria/<int:idmatPrima>', methods=["PATCH"])
def updateMateriaPrima(idmatPrima):
    dados_json = request.json
    
    if not dados_json:
        return jsonify({"erro": "Dados não recebidos corretamente, verifique as informações inseridas."}), 400
    
    try:
        mat_prima = db.session.get(materia_prima, idmatPrima)
        
        if mat_prima is None:
            return jsonify({"erro": f"Materia-prima com ID {idmatPrima} não encontrada."}), 404
        
        if 'nome' in dados_json:
            mat_prima.nome = dados_json['nome']
        if 'formula' in dados_json:
            mat_prima.formula = dados_json['formula']
        if 'quantidade' in dados_json:
            mat_prima.quantidade = dados_json['quantidade']
        if 'lote' in dados_json:
            mat_prima.lote = dados_json['lote']
        if 'data_validade' in dados_json:
            mat_prima.data_validade = dados_json['data_validade']
        
        db.session.commit()
        return jsonify(mat_prima.to_disc()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@materiaPrima_db.route("/materiaPrima/<string:nomeMatPrima>", methods=["GET"])
def buscarMatPrima(nomeMatPrima):
    try:
        stmt = db.select(materia_prima).where(materia_prima.nome == nomeMatPrima)
        mat_prima = db.session.execute(stmt).scalars().first()
        
        if mat_prima is None:
            return jsonify({"erro": f"Materia-prima '{nomeMatPrima}' não encontrada."}), 404
        
        return jsonify(mat_prima.to_disc()), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@materiaPrima_db.route("/materiaPrima/<int:idMatPrima>", methods=["DELETE"])
def deleteMateriaPrima(idMatPrima):
    try:
        mat_prima = db.session.get(materia_prima, idMatPrima)
        
        if mat_prima is None:
            return jsonify({"erro": f"Materia-prima com ID {idMatPrima} não encontrada."}), 404
        
        db.session.delete(mat_prima)
        db.session.commit()
        
        return jsonify({"mensagem": f"Materia-prima '{mat_prima.nome}' deletada com sucesso."}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500