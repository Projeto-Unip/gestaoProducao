from flask import Blueprint, jsonify, request
from models.producao import Producao
from models.statusProducao import StatusProducao
from models.pesquisa import Pesquisa
from database.dba import db
from datetime import datetime

producao_db = Blueprint('producao', __name__, url_prefix="/api")

@producao_db.route("/producoes", methods=["GET"])
def listar():
    try:
        stmt = db.select(Producao)
        producoes = db.session.execute(stmt).scalars().all()
        
        producoes_list = [p.to_disc(incluir_status=True, incluir_pesquisa=True) for p in producoes]
        return jsonify(producoes_list), 200
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return jsonify({"erro": "Ocorreu um erro ao buscar produções"}), 500


@producao_db.route("/addProducao", methods=["POST"])
def addProducao():
    try:
        dados = request.json
        
        if not dados:
            return jsonify({"erro": "Não foi possível identificar os dados enviados"}), 400
        
        # Verificar se o status existe
        status = db.session.get(StatusProducao, dados.get('idStatusProducao'))
        if not status:
            return jsonify({"erro": f"Status com ID {dados.get('idStatusProducao')} não encontrado."}), 404
        
        # Verificar se a pesquisa existe
        pesquisa = db.session.get(Pesquisa, dados.get('idPesquisa'))
        if not pesquisa:
            return jsonify({"erro": f"Pesquisa com ID {dados.get('idPesquisa')} não encontrada."}), 404
        
        # Converter strings de data para datetime
        data_inicio = datetime.fromisoformat(dados.get('dataInicio'))
        data_fim = datetime.fromisoformat(dados.get('dataFim'))
        
        novaProducao = Producao(
            nomeMediamento=dados.get('nomeMedicamento').strip(),
            descricaoMedicamento=dados.get('descricaoMedicamento'),
            data_inicio=data_inicio,
            data_fim=data_fim,
            id_statusProducao=dados.get('idStatusProducao'),
            id_pesquisa=dados.get('idPesquisa')
        )
        
        db.session.add(novaProducao)
        db.session.commit()
        
        return jsonify(novaProducao.to_disc(incluir_status=True, incluir_pesquisa=True)), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@producao_db.route('/updateProducao/<int:idProducao>', methods=["PATCH"])
def updateProducao(idProducao):
    dados_json = request.json
    
    if not dados_json:
        return jsonify({"erro": "Dados não recebidos corretamente, verifique as informações inseridas."}), 400
    
    try:
        producao = db.session.get(Producao, idProducao)
        
        if producao is None:
            return jsonify({"erro": f"Produção com ID {idProducao} não encontrada."}), 404
        
        if 'nomeMedicamento' in dados_json:
            producao.nomeMediamento = dados_json['nomeMedicamento'].strip()
        if 'descricaoMedicamento' in dados_json:
            producao.descricaoMedicamento = dados_json['descricaoMedicamento']
        if 'dataInicio' in dados_json:
            producao.data_inicio = datetime.fromisoformat(dados_json['dataInicio'])
        if 'dataFim' in dados_json:
            producao.data_fim = datetime.fromisoformat(dados_json['dataFim'])
        if 'idStatusProducao' in dados_json:
            status = db.session.get(StatusProducao, dados_json['idStatusProducao'])
            if not status:
                return jsonify({"erro": f"Status com ID {dados_json['idStatusProducao']} não encontrado."}), 404
            producao.id_statusProducao = dados_json['idStatusProducao']
        if 'idPesquisa' in dados_json:
            pesquisa = db.session.get(Pesquisa, dados_json['idPesquisa'])
            if not pesquisa:
                return jsonify({"erro": f"Pesquisa com ID {dados_json['idPesquisa']} não encontrada."}), 404
            producao.id_pesquisa = dados_json['idPesquisa']
        
        db.session.commit()
        return jsonify(producao.to_disc(incluir_status=True, incluir_pesquisa=True)), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@producao_db.route("/producao/<int:idProducao>", methods=["GET"])
def buscarProducao(idProducao):
    try:
        producao = db.session.get(Producao, idProducao)
        
        if producao is None:
            return jsonify({"erro": f"Produção com ID {idProducao} não encontrada."}), 404
        
        return jsonify(producao.to_disc(incluir_status=True, incluir_pesquisa=True)), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@producao_db.route("/producao/<int:idProducao>", methods=["DELETE"])
def deleteProducao(idProducao):
    try:
        producao = db.session.get(Producao, idProducao)
        
        if producao is None:
            return jsonify({"erro": f"Produção com ID {idProducao} não encontrada."}), 404
        
        db.session.delete(producao)
        db.session.commit()
        
        return jsonify({"mensagem": f"Produção '{producao.nomeMediamento}' deletada com sucesso."}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
