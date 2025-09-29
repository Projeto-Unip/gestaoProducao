from models.materialPrima import adicionar_medicamento, listar_medicamentos, buscar_medicamento, remover_medicamento

def criar_medicamento(data):
    novo = {
        "id": len(listar_medicamentos()) + 1,
        "nome": data.get("nome"),
        "quantidade": data.get("quantidade"),
        "preco": data.get("preco")
    }
    adicionar_medicamento(novo)
    return novo

def obter_medicamentos():
    return listar_medicamentos()

def obter_medicamento(id):
    return buscar_medicamento(id)

def deletar_medicamento(id):
    remover_medicamento(id)
    return {"mensagem": f"Medicamento {id} removido"}
