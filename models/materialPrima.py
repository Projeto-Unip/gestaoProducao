medicamentos = []

def adicionar_medicamento(med):
    medicamentos.append(med)

def listar_medicamentos():
    return medicamentos

def buscar_medicamento(id):
    for m in medicamentos:
        if m["id"] == id:
            return m
    return None

def remover_medicamento(id):
    global medicamentos
    medicamentos = [m for m in medicamentos if m["id"] != id]
