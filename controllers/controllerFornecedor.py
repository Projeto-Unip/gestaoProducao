from flask import Blueprint, jsonify, request
from models.fornecedor import Fornecedor
from database.dba import db

fornecedor_db = Blueprint('fornecedor', __name__, url_prefix="/api")

@fornecedor_db.route("/fornecedores", methods=["GET"])
def listar():
    try:
        stmt = db.select(Fornecedor)
        fornecedores = db.session.execute(stmt).scalars().all()
        
        fornecedores_list = [f.to_disc() for f in fornecedores]
        return jsonify(fornecedores_list), 200
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return jsonify({"erro": "Ocorreu um erro ao buscar fornecedores"}), 500


@fornecedor_db.route("/addFornecedor", methods=["POST"])
def addFornecedor():
    try:
        dados = request.json
        
        if not dados:
            return jsonify({"erro": "Não foi possível identificar os dados enviados"}), 400
        
        # Verificando se o fornecedor existe no dba por CNPJ
        cnpj_normalizado = dados.get('cnpj').strip()
        stmt = db.select(Fornecedor).where(Fornecedor.cnpj == cnpj_normalizado)
        existFornecedor = db.session.execute(stmt).scalars().first()
        
        if not existFornecedor:
            razao_normalizada = dados.get('razaoSocial').strip().lower()
            novoFornecedor = Fornecedor(
                razaoSocial=razao_normalizada,
                cnpj=cnpj_normalizado,
                contato=dados.get('contato')
            )
            
            db.session.add(novoFornecedor)
            db.session.commit()
            
            return jsonify(novoFornecedor.to_disc()), 201
        else:
            return jsonify({"mensagem": "Fornecedor já existe!"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@fornecedor_db.route('/updateFornecedor/<int:idFornecedor>', methods=["PATCH"])
def updateFornecedor(idFornecedor):
    dados_json = request.json
    
    if not dados_json:
        return jsonify({"erro": "Dados não recebidos corretamente, verifique as informações inseridas."}), 400
    
    try:
        fornecedor = db.session.get(Fornecedor, idFornecedor)
        
        if fornecedor is None:
            return jsonify({"erro": f"Fornecedor com ID {idFornecedor} não encontrado."}), 404
        
        if 'razaoSocial' in dados_json:
            fornecedor.razaoSocial = dados_json['razaoSocial'].strip().lower()
        if 'cnpj' in dados_json:
            fornecedor.cnpj = dados_json['cnpj'].strip()
        if 'contato' in dados_json:
            fornecedor.contato = dados_json['contato']
        
        db.session.commit()
        return jsonify(fornecedor.to_disc()), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500


@fornecedor_db.route("/fornecedor/<string:cnpj>", methods=["GET"])
def buscarFornecedor(cnpj):
    try:
        stmt = db.select(Fornecedor).where(Fornecedor.cnpj == cnpj)
        fornecedor = db.session.execute(stmt).scalars().first()
        
        if fornecedor is None:
            return jsonify({"erro": f"Fornecedor com CNPJ '{cnpj}' não encontrado."}), 404
        
        return jsonify(fornecedor.to_disc()), 200
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@fornecedor_db.route("/fornecedor/<int:idFornecedor>", methods=["DELETE"])
def deleteFornecedor(idFornecedor):
    try:
        fornecedor = db.session.get(Fornecedor, idFornecedor)
        
        if fornecedor is None:
            return jsonify({"erro": f"Fornecedor com ID {idFornecedor} não encontrado."}), 404
        
        db.session.delete(fornecedor)
        db.session.commit()
        
        return jsonify({"mensagem": f"Fornecedor '{fornecedor.razaoSocial}' deletado com sucesso."}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500
