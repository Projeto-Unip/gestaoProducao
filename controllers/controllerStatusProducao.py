from flask import Blueprint, jsonify, request
from models.statusProducao import StatusProducao
from database.dba import db

statusProducao_db = Blueprint('statusProducao', __name__, url_prefix="/api")

@statusProducao_db.route("/status", methods=["GET"])
def listar():
    try:
        stmt = db.select(StatusProducao)
        status_list = db.session.execute(stmt).scalars().all()
        
        status_data = [s.to_disc() for s in status_list]
        return jsonify(status_data), 200
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return jsonify({"erro": "Ocorreu um erro ao buscar status"}), 500


@statusProducao_db.route("/addStatus", methods=["POST"])
def addStatus():
    try:
        dados = request.json
        
        if not dados:
            return jsonify({"erro": "Não foi possível identificar os dados enviados"}), 400
        
        nome_normalizado = dados.get('nomeStatus').strip().lower()
        stmt = db.select(StatusProducao).where(StatusProducao.nomeStatus == nome_normalizado)
        existStatus = db.session.execute(stmt).scalars().first()
        
        if not existStatus:
            novoStatus = StatusProducao(
                nomeStatus=nome_normalizado,
                descricaoStatus=dados.get('descricaoStatus')
            )
            
            db.session.add(novoStatus)
            db.session.commit()
            
            return jsonify(novoStatus.to_disc()), 201
        else:
            return jsonify({"mensagem": "Status já existe!"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@statusProducao_db.route('/updateStatus/<int:idStatus>', methods=["PATCH"])
def updateStatus(idStatus):
    dados_json = request.json
    
    if not dados_json:
        return jsonify({"erro": "Dados não recebidos corretamente, verifique as informações inseridas."}), 400
    
    try:
        status = db.session.get(StatusProducao, idStatus)
        
        if status is None:
            return jsonify({"erro": f"Status com ID {idStatus} não encontrado."}), 404
        
        if 'nomeStatus' in dados_json:
            status.nomeStatus = dados_json['nomeStatus'].strip().lower()
        if 'descricaoStatus' in dados_json:
            status.descricaoStatus = dados_json['descricaoStatus']
        
        db.session.commit()
        return jsonify(status.to_disc()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@statusProducao_db.route("/status/<int:idStatus>", methods=["GET"])
def buscarStatus(idStatus):
    try:
        status = db.session.get(StatusProducao, idStatus)
        
        if status is None:
            return jsonify({"erro": f"Status com ID {idStatus} não encontrado."}), 404
        
        return jsonify(status.to_disc()), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@statusProducao_db.route("/status/<int:idStatus>", methods=["DELETE"])
def deleteStatus(idStatus):
    try:
        status = db.session.get(StatusProducao, idStatus)
        
        if status is None:
            return jsonify({"erro": f"Status com ID {idStatus} não encontrado."}), 404
        
        db.session.delete(status)
        db.session.commit()
        
        return jsonify({"mensagem": f"Status '{status.nomeStatus}' deletado com sucesso."}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
