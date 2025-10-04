from flask import Blueprint, jsonify, request
from models.etapaPesquisa import EtapaPesquisa
from database.dba import db

etapaPesquisa_db = Blueprint('etapaPesquisa', __name__, url_prefix="/api")

@etapaPesquisa_db.route("/etapas", methods=["GET"])
def listar():
    try:
        stmt = db.select(EtapaPesquisa)
        etapas = db.session.execute(stmt).scalars().all()
        
        etapas_list = [e.to_disc() for e in etapas]
        return jsonify(etapas_list), 200
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return jsonify({"erro": "Ocorreu um erro ao buscar etapas"}), 500


@etapaPesquisa_db.route("/addEtapa", methods=["POST"])
def addEtapa():
    try:
        dados = request.json
        
        if not dados:
            return jsonify({"erro": "Não foi possível identificar os dados enviados"}), 400
        
        nome_normalizado = dados.get('nomeEtapa').strip().lower()
        stmt = db.select(EtapaPesquisa).where(EtapaPesquisa.nome_etapa == nome_normalizado)
        existEtapa = db.session.execute(stmt).scalars().first()
        
        if not existEtapa:
            novaEtapa = EtapaPesquisa(
                nome_etapa=nome_normalizado,
                descricao_etapa=dados.get('descricaoEtapa')
            )
            
            db.session.add(novaEtapa)
            db.session.commit()
            
            return jsonify(novaEtapa.to_disc()), 201
        else:
            return jsonify({"mensagem": "Etapa já existe!"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@etapaPesquisa_db.route('/updateEtapa/<int:idEtapa>', methods=["PATCH"])
def updateEtapa(idEtapa):
    dados_json = request.json
    
    if not dados_json:
        return jsonify({"erro": "Dados não recebidos corretamente, verifique as informações inseridas."}), 400
    
    try:
        etapa = db.session.get(EtapaPesquisa, idEtapa)
        
        if etapa is None:
            return jsonify({"erro": f"Etapa com ID {idEtapa} não encontrada."}), 404
        
        if 'nomeEtapa' in dados_json:
            etapa.nome_etapa = dados_json['nomeEtapa'].strip().lower()
        if 'descricaoEtapa' in dados_json:
            etapa.descricao_etapa = dados_json['descricaoEtapa']
        
        db.session.commit()
        return jsonify(etapa.to_disc()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@etapaPesquisa_db.route("/etapa/<int:idEtapa>", methods=["GET"])
def buscarEtapa(idEtapa):
    try:
        etapa = db.session.get(EtapaPesquisa, idEtapa)
        
        if etapa is None:
            return jsonify({"erro": f"Etapa com ID {idEtapa} não encontrada."}), 404
        
        return jsonify(etapa.to_disc()), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@etapaPesquisa_db.route("/etapa/<int:idEtapa>", methods=["DELETE"])
def deleteEtapa(idEtapa):
    try:
        etapa = db.session.get(EtapaPesquisa, idEtapa)
        
        if etapa is None:
            return jsonify({"erro": f"Etapa com ID {idEtapa} não encontrada."}), 404
        
        db.session.delete(etapa)
        db.session.commit()
        
        return jsonify({"mensagem": f"Etapa '{etapa.nome_etapa}' deletada com sucesso."}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
