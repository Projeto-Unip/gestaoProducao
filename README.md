# 💊 Sistema de Gestão de Produção Farmacêutica

Web Application desenvolvido para realizar gestão completa de produção de medicamentos, desde a fase de pesquisa e desenvolvimento até a produção final, incluindo controle de insumos, fornecedores e etapas do processo.

---

## 📋 Sobre o Projeto

Sistema acadêmico (PIM III) desenvolvido com Flask para gerenciar todo o ciclo de produção farmacêutica, permitindo:

- Controle de matérias-primas e fornecedores
- Gestão de pesquisas e desenvolvimento de medicamentos
- Acompanhamento de etapas de pesquisa
- Monitoramento do status de produção
- Rastreabilidade de insumos utilizados em cada pesquisa

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.x**
- **Flask** - Framework web
- **SQLAlchemy** - ORM para banco de dados
- **MySQL** - Banco de dados relacional
- **python-dotenv** - Gerenciamento de variáveis de ambiente

### Arquitetura
- **MVC** (Model-View-Controller)
- **API RESTful**
- **Relacionamentos N:N** (Many-to-Many)

---

## 📁 Estrutura do Projeto

```
gestaoProducao/
├── controllers/
│   ├── controllerMaterialPrima.py
│   ├── controllerFornecedor.py
│   ├── controllerVinculo.py
│   ├── controllerEtapaPesquisa.py
│   ├── controllerStatusProducao.py
│   ├── controllerPesquisa.py
│   └── controllerProducao.py
├── models/
│   ├── materialPrima.py
│   ├── fornecedor.py
│   ├── etapaPesquisa.py
│   ├── statusProducao.py
│   ├── pesquisa.py
│   └── producao.py
├── database/
│   └── dba.py
├── app.py
├── .env
└── README.md

frontend/
├── DOCUMENTACAO_API.md
└── GUIA_JAVASCRIPT.md
```

---

## 🗄️ Modelo de Dados

### Entidades Principais

1. **Matéria-Prima**
   - Controle de insumos químicos
   - Rastreamento por lote e validade

2. **Fornecedor**
   - Cadastro de fornecedores
   - Vínculo N:N com matérias-primas

3. **Etapa de Pesquisa**
   - Fases do desenvolvimento (P&D, Testes, Aprovação, etc.)

4. **Pesquisa**
   - Projetos de desenvolvimento de medicamentos
   - Vínculo N:N com matérias-primas utilizadas

5. **Status de Produção**
   - Estados do processo (Em Andamento, Concluído, Pausado, etc.)

6. **Produção**
   - Lotes de medicamentos produzidos
   - Relacionado a pesquisas específicas

### Relacionamentos

- **Fornecedor ↔ Matéria-Prima** (N:N via `fornecedor_materiaPrima`)
- **Pesquisa ↔ Matéria-Prima** (N:N via `pesquisa_materiaPrima`)
- **Pesquisa → Etapa de Pesquisa** (N:1)
- **Produção → Pesquisa** (N:1)
- **Produção → Status de Produção** (N:1)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- MySQL Server
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/Projeto-Unip/gestaoProducao.git
cd gestaoProducao
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install flask flask-sqlalchemy pymysql python-dotenv flask-cors
```

5. **Configure o banco de dados:**

Crie um arquivo `.env` na raiz do projeto:
```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=gestao_producao
SECRET_KEY=sua_chave_secreta
```

6. **Execute os scripts SQL:**

Execute os scripts da pasta `DBA/` para criar as tabelas no MySQL.

7. **Inicie o servidor:**
```bash
python app.py
```

O servidor estará rodando em: `http://localhost:5000`

---

## 📚 Documentação da API

### URL Base
```
http://localhost:5000/api
```

### Endpoints Disponíveis

#### 📦 Matéria-Prima
- `GET /materia-prima` - Listar todas
- `POST /addMateriaPrima` - Adicionar
- `PATCH /updateMateria/<id>` - Atualizar
- `GET /materiaPrima/<nome>` - Buscar por nome
- `DELETE /materiaPrima/<id>` - Deletar

#### 🏭 Fornecedor
- `GET /fornecedores` - Listar todos
- `POST /addFornecedor` - Adicionar
- `PATCH /updateFornecedor/<id>` - Atualizar
- `GET /fornecedor/<cnpj>` - Buscar por CNPJ
- `DELETE /fornecedor/<id>` - Deletar

#### 🔗 Vínculos (Fornecedor ↔ Material)
- `POST /vincularMaterial` - Vincular
- `DELETE /desvincularMaterial` - Desvincular
- `GET /fornecedor/<id>/materiais` - Materiais do fornecedor
- `GET /material/<id>/fornecedores` - Fornecedores do material

#### 📊 Etapa de Pesquisa
- `GET /etapas` - Listar todas
- `POST /addEtapa` - Adicionar
- `PATCH /updateEtapa/<id>` - Atualizar
- `GET /etapa/<id>` - Buscar por ID
- `DELETE /etapa/<id>` - Deletar

#### ⚙️ Status de Produção
- `GET /status` - Listar todos
- `POST /addStatus` - Adicionar
- `PATCH /updateStatus/<id>` - Atualizar
- `GET /status/<id>` - Buscar por ID
- `DELETE /status/<id>` - Deletar

#### 🔬 Pesquisa
- `GET /pesquisas` - Listar todas
- `POST /addPesquisa` - Adicionar
- `PATCH /updatePesquisa/<id>` - Atualizar
- `GET /pesquisa/<id>` - Buscar por ID
- `DELETE /pesquisa/<id>` - Deletar
- `POST /pesquisa/<id>/vincularMaterial` - Vincular material
- `DELETE /pesquisa/<id>/desvincularMaterial/<idMaterial>` - Desvincular

#### 🏭 Produção
- `GET /producoes` - Listar todas
- `POST /addProducao` - Adicionar
- `PATCH /updateProducao/<id>` - Atualizar
- `GET /producao/<id>` - Buscar por ID
- `DELETE /producao/<id>` - Deletar

**Documentação completa:** Veja `frontend/DOCUMENTACAO_API.md`

**Guia JavaScript:** Veja `frontend/GUIA_JAVASCRIPT.md`

---

## 🧪 Exemplos de Uso

### Adicionar Matéria-Prima

```bash
curl -X POST http://localhost:5000/api/addMateriaPrima \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Acido Sulfurico",
    "formula": "H2SO4",
    "quantidade": 100,
    "lote": "L001",
    "data_validade": "2025-12-31"
  }'
```

### Vincular Fornecedor a Material

```bash
curl -X POST http://localhost:5000/api/vincularMaterial \
  -H "Content-Type: application/json" \
  -d '{
    "id_fornecedor": 1,
    "id_materiaPrima": 1
  }'
```

---

## ✅ Funcionalidades Implementadas

- [x] CRUD completo de Matéria-Prima
- [x] CRUD completo de Fornecedor
- [x] Relacionamento N:N entre Fornecedor e Matéria-Prima
- [x] CRUD completo de Etapa de Pesquisa
- [x] CRUD completo de Status de Produção
- [x] CRUD completo de Pesquisa
- [x] Relacionamento N:N entre Pesquisa e Matéria-Prima
- [x] CRUD completo de Produção
- [x] Validação de dados e tratamento de erros
- [x] Normalização de dados (lowercase, trim)
- [x] Endpoints de listagem com relacionamentos

---

## 🔒 Segurança

- Validação de entrada de dados
- Tratamento de exceções
- Rollback automático em caso de erro
- Normalização de dados para evitar duplicatas

---

## 🎓 Projeto Acadêmico

Este projeto foi desenvolvido como parte do **Projeto Integrado Multidisciplinar III (PIM III)** do curso de Análise e Desenvolvimento de Sistemas.

**Objetivo:** Demonstrar conhecimentos em:
- Desenvolvimento de APIs RESTful
- Modelagem de banco de dados relacional
- Arquitetura MVC
- Relacionamentos complexos entre entidades
- Boas práticas de desenvolvimento backend

---

## 👥 Autor

Desenvolvido por estudantes de ADS - UNIP
Autor: Jhonatan Oliveira Silva

---

## 📄 Licença

Este projeto é de uso acadêmico e educacional.

---

## 🤝 Contribuições

Este é um projeto acadêmico. Sugestões e melhorias são bem-vindas através de issues e pull requests.

---

## 📞 Suporte

Para dúvidas sobre a API, consulte:
- `frontend/DOCUMENTACAO_API.md` - Documentação completa dos endpoints
- `frontend/GUIA_JAVASCRIPT.md` - Exemplos de integração com JavaScript
