from flask import Blueprint, jsonify, request
from models.pesquisa import Pesquisa
from models.etapaPesquisa import EtapaPesquisa
from models.materialPrima import materia_prima
from database.dba import db
from datetime import datetime

pesquisa_db = Blueprint('pesquisa', __name__, url_prefix="/api")

@pesquisa_db.route("/pesquisas", methods=["GET"])
def listar():
    try:
        stmt = db.select(Pesquisa)
        pesquisas = db.session.execute(stmt).scalars().all()
        
        pesquisas_list = [p.to_disc(incluir_etapa=True) for p in pesquisas]
        return jsonify(pesquisas_list), 200
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return jsonify({"erro": "Ocorreu um erro ao buscar pesquisas"}), 500


@pesquisa_db.route("/addPesquisa", methods=["POST"])
def addPesquisa():
    try:
        dados = request.json
        
        if not dados:
            return jsonify({"erro": "Não foi possível identificar os dados enviados"}), 400
        
        # Verificar se a etapa existe
        etapa = db.session.get(EtapaPesquisa, dados.get('idEtapaPesquisa'))
        if not etapa:
            return jsonify({"erro": f"Etapa com ID {dados.get('idEtapaPesquisa')} não encontrada."}), 404
        
        # Converter strings de data para datetime
        data_inicio = datetime.fromisoformat(dados.get('dataInicio'))
        data_fim = datetime.fromisoformat(dados.get('dataFim'))
        
        novaPesquisa = Pesquisa(
            nome_pesquisa=dados.get('nomePesquisa').strip(),
            descricao=dados.get('descricao'),
            data_inicio=data_inicio,
            data_fim=data_fim,
            id_etapaPesquisa=dados.get('idEtapaPesquisa')
        )
        
        db.session.add(novaPesquisa)
        db.session.commit()
        
        return jsonify(novaPesquisa.to_disc(incluir_etapa=True)), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@pesquisa_db.route('/updatePesquisa/<int:idPesquisa>', methods=["PATCH"])
def updatePesquisa(idPesquisa):
    dados_json = request.json
    
    if not dados_json:
        return jsonify({"erro": "Dados não recebidos corretamente, verifique as informações inseridas."}), 400
    
    try:
        pesquisa = db.session.get(Pesquisa, idPesquisa)
        
        if pesquisa is None:
            return jsonify({"erro": f"Pesquisa com ID {idPesquisa} não encontrada."}), 404
        
        if 'nomePesquisa' in dados_json:
            pesquisa.nome_pesquisa = dados_json['nomePesquisa'].strip()
        if 'descricao' in dados_json:
            pesquisa.descricao = dados_json['descricao']
        if 'dataInicio' in dados_json:
            pesquisa.data_inicio = datetime.fromisoformat(dados_json['dataInicio'])
        if 'dataFim' in dados_json:
            pesquisa.data_fim = datetime.fromisoformat(dados_json['dataFim'])
        if 'idEtapaPesquisa' in dados_json:
            etapa = db.session.get(EtapaPesquisa, dados_json['idEtapaPesquisa'])
            if not etapa:
                return jsonify({"erro": f"Etapa com ID {dados_json['idEtapaPesquisa']} não encontrada."}), 404
            pesquisa.id_etapaPesquisa = dados_json['idEtapaPesquisa']
        
        db.session.commit()
        return jsonify(pesquisa.to_disc(incluir_etapa=True)), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@pesquisa_db.route("/pesquisa/<int:idPesquisa>", methods=["GET"])
def buscarPesquisa(idPesquisa):
    try:
        pesquisa = db.session.get(Pesquisa, idPesquisa)
        
        if pesquisa is None:
            return jsonify({"erro": f"Pesquisa com ID {idPesquisa} não encontrada."}), 404
        
        return jsonify(pesquisa.to_disc(incluir_etapa=True, incluir_materiais=True)), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@pesquisa_db.route("/pesquisa/<int:idPesquisa>", methods=["DELETE"])
def deletePesquisa(idPesquisa):
    try:
        pesquisa = db.session.get(Pesquisa, idPesquisa)
        
        if pesquisa is None:
            return jsonify({"erro": f"Pesquisa com ID {idPesquisa} não encontrada."}), 404
        
        db.session.delete(pesquisa)
        db.session.commit()
        
        return jsonify({"mensagem": f"Pesquisa '{pesquisa.nome_pesquisa}' deletada com sucesso."}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


# Endpoints para vincular materiais à pesquisa
@pesquisa_db.route("/pesquisa/<int:idPesquisa>/vincularMaterial", methods=["POST"])
def vincularMaterial(idPesquisa):
    try:
        dados = request.json
        
        if not dados or 'idMaterial' not in dados:
            return jsonify({"erro": "Envie o idMaterial no corpo da requisição"}), 400
        
        pesquisa = db.session.get(Pesquisa, idPesquisa)
        material = db.session.get(materia_prima, dados['idMaterial'])
        
        if not pesquisa:
            return jsonify({"erro": f"Pesquisa com ID {idPesquisa} não encontrada."}), 404
        
        if not material:
            return jsonify({"erro": f"Material com ID {dados['idMaterial']} não encontrado."}), 404
        
        if material in pesquisa.materiais:
            return jsonify({"mensagem": "Material já vinculado a esta pesquisa!"}), 200
        
        pesquisa.materiais.append(material)
        db.session.commit()
        
        return jsonify({"mensagem": f"Material '{material.nome}' vinculado à pesquisa '{pesquisa.nome_pesquisa}' com sucesso."}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@pesquisa_db.route("/pesquisa/<int:idPesquisa>/desvincularMaterial/<int:idMaterial>", methods=["DELETE"])
def desvincularMaterial(idPesquisa, idMaterial):
    try:
        pesquisa = db.session.get(Pesquisa, idPesquisa)
        material = db.session.get(materia_prima, idMaterial)
        
        if not pesquisa:
            return jsonify({"erro": f"Pesquisa com ID {idPesquisa} não encontrada."}), 404
        
        if not material:
            return jsonify({"erro": f"Material com ID {idMaterial} não encontrado."}), 404
        
        if material not in pesquisa.materiais:
            return jsonify({"erro": "Material não está vinculado a esta pesquisa!"}), 404
        
        pesquisa.materiais.remove(material)
        db.session.commit()
        
        return jsonify({"mensagem": f"Material '{material.nome}' desvinculado da pesquisa '{pesquisa.nome_pesquisa}' com sucesso."}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
