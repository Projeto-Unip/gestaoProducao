# Documentação API - Sistema de Gestão de Produção Farmacêutica

## URL Base
```
http://localhost:5000/api
```

---

## 📦 MATÉRIA-PRIMA

### 1. Listar todas as matérias-primas
**GET** `/api/materia-prima`

**Resposta (200):**
```json
[
  {
    "id": 1,
    "nome": "acido sulfurico",
    "formula": "H2SO4",
    "quantidade": 100,
    "lote": "L001",
    "dataValidade": "2025-12-31"
  }
]
```

---

### 2. Adicionar matéria-prima
**POST** `/api/addMateriaPrima`

**Corpo da requisição:**
```json
{
  "nome": "Acido Sulfurico",
  "formula": "H2SO4",
  "quantidade": 100,
  "lote": "L001",
  "data_validade": "2025-12-31"
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "nome": "acido sulfurico",
  "formula": "H2SO4",
  "quantidade": 100,
  "lote": "L001",
  "dataValidade": "2025-12-31"
}
```

---

### 3. Atualizar matéria-prima
**PATCH** `/api/updateMateria/<id>`

**Corpo da requisição:**
```json
{
  "quantidade": 150,
  "lote": "L002"
}
```

**Resposta (200):**
```json
{
  "id": 1,
  "nome": "acido sulfurico",
  "formula": "H2SO4",
  "quantidade": 150,
  "lote": "L002",
  "dataValidade": "2025-12-31"
}
```

---

### 4. Buscar matéria-prima por nome
**GET** `/api/materiaPrima/<nome>`

**Exemplo:** `/api/materiaPrima/acido%20sulfurico`

**Resposta (200):**
```json
{
  "id": 1,
  "nome": "acido sulfurico",
  "formula": "H2SO4",
  "quantidade": 100,
  "lote": "L001",
  "dataValidade": "2025-12-31"
}
```

---

### 5. Deletar matéria-prima
**DELETE** `/api/materiaPrima/<id>`

**Resposta (200):**
```json
{
  "mensagem": "Materia-prima 'acido sulfurico' deletada com sucesso."
}
```

---

## 🏭 FORNECEDOR

### 1. Listar fornecedores
**GET** `/api/fornecedores`

**Resposta (200):**
```json
[
  {
    "id": 1,
    "razaoSocial": "quimica brasil ltda",
    "cnpj": "12.345.678/0001-99",
    "contato": "(11) 98765-4321"
  }
]
```

---

### 2. Adicionar fornecedor
**POST** `/api/addFornecedor`

**Corpo da requisição:**
```json
{
  "razaoSocial": "Quimica Brasil LTDA",
  "cnpj": "12.345.678/0001-99",
  "contato": "(11) 98765-4321"
}
```

**Resposta (201):**
```json
{
  "id": 1,
  "razaoSocial": "quimica brasil ltda",
  "cnpj": "12.345.678/0001-99",
  "contato": "(11) 98765-4321"
}
```

---

### 3. Atualizar fornecedor
**PATCH** `/api/updateFornecedor/<id>`

**Corpo da requisição:**
```json
{
  "contato": "(11) 91111-2222"
}
```

---

### 4. Buscar fornecedor por CNPJ
**GET** `/api/fornecedor/<cnpj>`

**Exemplo:** `/api/fornecedor/12.345.678/0001-99`

---

### 5. Deletar fornecedor
**DELETE** `/api/fornecedor/<id>`

**Resposta (200):**
```json
{
  "mensagem": "Fornecedor 'quimica brasil ltda' deletado com sucesso."
}
```

---

## 🔗 VÍNCULOS (Fornecedor ↔ Material)

### 1. Vincular material a fornecedor
**POST** `/api/vincularMaterial`

**Corpo da requisição:**
```json
{
  "id_fornecedor": 1,
  "id_materiaPrima": 1
}
```

**Resposta (201):**
```json
{
  "mensagem": "Material 'acido sulfurico' vinculado ao fornecedor 'quimica brasil ltda' com sucesso."
}
```

---

### 2. Desvincular material de fornecedor
**DELETE** `/api/desvincularMaterial`

**Corpo da requisição:**
```json
{
  "id_fornecedor": 1,
  "id_materiaPrima": 1
}
```

---

### 3. Listar materiais de um fornecedor
**GET** `/api/fornecedor/<id>/materiais`

**Resposta (200):**
```json
{
  "fornecedor": "quimica brasil ltda",
  "materiais": [
    {
      "id": 1,
      "nome": "acido sulfurico",
      "formula": "H2SO4",
      "quantidade": 100,
      "lote": "L001",
      "dataValidade": "2025-12-31"
    }
  ]
}
```

---

### 4. Listar fornecedores de um material
**GET** `/api/material/<id>/fornecedores`

**Resposta (200):**
```json
{
  "material": "acido sulfurico",
  "fornecedores": [
    {
      "id": 1,
      "razaoSocial": "quimica brasil ltda",
      "cnpj": "12.345.678/0001-99",
      "contato": "(11) 98765-4321"
    }
  ]
}
```

---

## 📊 ETAPA DE PESQUISA

### 1. Listar etapas
**GET** `/api/etapas`

---

### 2. Adicionar etapa
**POST** `/api/addEtapa`

**Corpo da requisição:**
```json
{
  "nomeEtapa": "Pesquisa e Desenvolvimento",
  "descricaoEtapa": "Fase inicial de desenvolvimento do medicamento"
}
```

---

### 3. Atualizar etapa
**PATCH** `/api/updateEtapa/<id>`

---

### 4. Buscar etapa
**GET** `/api/etapa/<id>`

---

### 5. Deletar etapa
**DELETE** `/api/etapa/<id>`

---

## ⚙️ STATUS DE PRODUÇÃO

### 1. Listar status
**GET** `/api/status`

---

### 2. Adicionar status
**POST** `/api/addStatus`

**Corpo da requisição:**
```json
{
  "nomeStatus": "Em Andamento",
  "descricaoStatus": "Produção em andamento"
}
```

---

### 3. Atualizar status
**PATCH** `/api/updateStatus/<id>`

---

### 4. Buscar status
**GET** `/api/status/<id>`

---

### 5. Deletar status
**DELETE** `/api/status/<id>`

---

## 🔬 PESQUISA

### 1. Listar pesquisas
**GET** `/api/pesquisas`

**Resposta (200):**
```json
[
  {
    "id": 1,
    "nomePesquisa": "Vacina COVID-19",
    "descricao": "Desenvolvimento de vacina",
    "dataInicio": "2024-01-01T00:00:00",
    "dataFim": "2024-12-31T00:00:00",
    "idEtapaPesquisa": 1,
    "etapa": {
      "id": 1,
      "nomeEtapa": "pesquisa e desenvolvimento",
      "descricaoEtapa": "Fase inicial"
    }
  }
]
```

---

### 2. Adicionar pesquisa
**POST** `/api/addPesquisa`

**Corpo da requisição:**
```json
{
  "nomePesquisa": "Vacina COVID-19",
  "descricao": "Desenvolvimento de vacina",
  "dataInicio": "2024-01-01T00:00:00",
  "dataFim": "2024-12-31T00:00:00",
  "idEtapaPesquisa": 1
}
```

---

### 3. Atualizar pesquisa
**PATCH** `/api/updatePesquisa/<id>`

**Corpo da requisição:**
```json
{
  "dataFim": "2025-06-30T00:00:00",
  "idEtapaPesquisa": 2
}
```

---

### 4. Buscar pesquisa
**GET** `/api/pesquisa/<id>`

**Resposta (200):** Inclui etapa e materiais vinculados

---

### 5. Deletar pesquisa
**DELETE** `/api/pesquisa/<id>`

---

### 6. Vincular material à pesquisa
**POST** `/api/pesquisa/<id>/vincularMaterial`

**Corpo da requisição:**
```json
{
  "idMaterial": 1
}
```

---

### 7. Desvincular material da pesquisa
**DELETE** `/api/pesquisa/<idPesquisa>/desvincularMaterial/<idMaterial>`

---

## 🏭 PRODUÇÃO

### 1. Listar produções
**GET** `/api/producoes`

**Resposta (200):**
```json
[
  {
    "id": 1,
    "nomeMedicamento": "Vacina XYZ",
    "descricaoMedicamento": "Vacina para COVID-19",
    "dataInicio": "2024-06-01T00:00:00",
    "dataFim": "2024-12-31T00:00:00",
    "idStatusProducao": 1,
    "idPesquisa": 1,
    "status": {
      "id": 1,
      "nomeStatus": "em andamento",
      "descricaoStatus": "Produção em andamento"
    },
    "pesquisa": {
      "id": 1,
      "nomePesquisa": "Vacina COVID-19"
    }
  }
]
```

---

### 2. Adicionar produção
**POST** `/api/addProducao`

**Corpo da requisição:**
```json
{
  "nomeMedicamento": "Vacina XYZ",
  "descricaoMedicamento": "Vacina para COVID-19",
  "dataInicio": "2024-06-01T00:00:00",
  "dataFim": "2024-12-31T00:00:00",
  "idStatusProducao": 1,
  "idPesquisa": 1
}
```

---

### 3. Atualizar produção
**PATCH** `/api/updateProducao/<id>`

**Corpo da requisição:**
```json
{
  "idStatusProducao": 2,
  "dataFim": "2025-01-15T00:00:00"
}
```

---

### 4. Buscar produção
**GET** `/api/producao/<id>`

---

### 5. Deletar produção
**DELETE** `/api/producao/<id>`

---

## ⚠️ Códigos de Status HTTP

- **200** - Sucesso
- **201** - Criado com sucesso
- **400** - Dados inválidos ou incompletos
- **404** - Não encontrado
- **500** - Erro interno do servidor

---

## 📝 Observações

1. **Normalização de nomes:** Os nomes são salvos em minúsculas e sem espaços extras
2. **Datas:** Use formato ISO 8601 (`YYYY-MM-DDTHH:MM:SS`)
3. **Foreign Keys:** Sempre verifique se os IDs referenciados existem antes de criar registros
4. **Vínculos N:N:** Use os endpoints específicos de vínculo para relacionar entidades
