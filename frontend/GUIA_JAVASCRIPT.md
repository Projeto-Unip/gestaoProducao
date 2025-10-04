# Guia de Uso da API com JavaScript

Este guia demonstra como consumir a API REST usando JavaScript com **Fetch API** (nativo) e **Axios** (biblioteca).

---

## 🚀 Configuração Inicial

### Usando Fetch API (Nativo - não precisa instalar nada)

```javascript
const API_URL = 'http://localhost:5000/api';
```

### Usando Axios (Recomendado)

**Instalação:**
```bash
npm install axios
```

**Importação:**
```javascript
import axios from 'axios';

const API_URL = 'http://localhost:5000/api';
```

---

## 📦 MATÉRIA-PRIMA

### 1. Listar todas as matérias-primas

**Com Fetch:**
```javascript
async function listarMateriais() {
  try {
    const response = await fetch(`${API_URL}/materia-prima`);
    const materiais = await response.json();
    console.log(materiais);
    return materiais;
  } catch (error) {
    console.error('Erro ao listar materiais:', error);
  }
}

// Usar
listarMateriais();
```

**Com Axios:**
```javascript
async function listarMateriais() {
  try {
    const response = await axios.get(`${API_URL}/materia-prima`);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error('Erro ao listar materiais:', error.response?.data || error.message);
  }
}
```

---

### 2. Adicionar matéria-prima

**Com Fetch:**
```javascript
async function adicionarMaterial(dados) {
  try {
    const response = await fetch(`${API_URL}/addMateriaPrima`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dados)
    });
    
    const resultado = await response.json();
    console.log('Material adicionado:', resultado);
    return resultado;
  } catch (error) {
    console.error('Erro ao adicionar material:', error);
  }
}

// Exemplo de uso
adicionarMaterial({
  nome: "Acido Sulfurico",
  formula: "H2SO4",
  quantidade: 100,
  lote: "L001",
  data_validade: "2025-12-31"
});
```

**Com Axios:**
```javascript
async function adicionarMaterial(dados) {
  try {
    const response = await axios.post(`${API_URL}/addMateriaPrima`, dados);
    console.log('Material adicionado:', response.data);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}

// Exemplo de uso
adicionarMaterial({
  nome: "Acido Sulfurico",
  formula: "H2SO4",
  quantidade: 100,
  lote: "L001",
  data_validade: "2025-12-31"
});
```

---

### 3. Atualizar matéria-prima

**Com Fetch:**
```javascript
async function atualizarMaterial(id, dados) {
  try {
    const response = await fetch(`${API_URL}/updateMateria/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dados)
    });
    
    const resultado = await response.json();
    console.log('Material atualizado:', resultado);
    return resultado;
  } catch (error) {
    console.error('Erro ao atualizar material:', error);
  }
}

// Exemplo de uso
atualizarMaterial(1, {
  quantidade: 150,
  lote: "L002"
});
```

**Com Axios:**
```javascript
async function atualizarMaterial(id, dados) {
  try {
    const response = await axios.patch(`${API_URL}/updateMateria/${id}`, dados);
    console.log('Material atualizado:', response.data);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

---

### 4. Buscar matéria-prima por nome

**Com Fetch:**
```javascript
async function buscarMaterialPorNome(nome) {
  try {
    const nomeEncoded = encodeURIComponent(nome);
    const response = await fetch(`${API_URL}/materiaPrima/${nomeEncoded}`);
    const material = await response.json();
    console.log('Material encontrado:', material);
    return material;
  } catch (error) {
    console.error('Erro ao buscar material:', error);
  }
}

// Exemplo
buscarMaterialPorNome("acido sulfurico");
```

**Com Axios:**
```javascript
async function buscarMaterialPorNome(nome) {
  try {
    const response = await axios.get(`${API_URL}/materiaPrima/${encodeURIComponent(nome)}`);
    console.log('Material encontrado:', response.data);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

---

### 5. Deletar matéria-prima

**Com Fetch:**
```javascript
async function deletarMaterial(id) {
  try {
    const response = await fetch(`${API_URL}/materiaPrima/${id}`, {
      method: 'DELETE'
    });
    
    const resultado = await response.json();
    console.log('Material deletado:', resultado);
    return resultado;
  } catch (error) {
    console.error('Erro ao deletar material:', error);
  }
}

// Exemplo
deletarMaterial(1);
```

**Com Axios:**
```javascript
async function deletarMaterial(id) {
  try {
    const response = await axios.delete(`${API_URL}/materiaPrima/${id}`);
    console.log('Material deletado:', response.data);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

---

## 🏭 FORNECEDOR

### Listar fornecedores

**Com Axios:**
```javascript
async function listarFornecedores() {
  try {
    const response = await axios.get(`${API_URL}/fornecedores`);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

### Adicionar fornecedor

**Com Axios:**
```javascript
async function adicionarFornecedor(dados) {
  try {
    const response = await axios.post(`${API_URL}/addFornecedor`, {
      razaoSocial: dados.razaoSocial,
      cnpj: dados.cnpj,
      contato: dados.contato
    });
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}

// Exemplo
adicionarFornecedor({
  razaoSocial: "Quimica Brasil LTDA",
  cnpj: "12.345.678/0001-99",
  contato: "(11) 98765-4321"
});
```

### Atualizar fornecedor

**Com Axios:**
```javascript
async function atualizarFornecedor(id, dados) {
  try {
    const response = await axios.patch(`${API_URL}/updateFornecedor/${id}`, dados);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

### Buscar fornecedor por CNPJ

**Com Axios:**
```javascript
async function buscarFornecedorPorCNPJ(cnpj) {
  try {
    const response = await axios.get(`${API_URL}/fornecedor/${encodeURIComponent(cnpj)}`);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}

// Exemplo
buscarFornecedorPorCNPJ("12.345.678/0001-99");
```

### Deletar fornecedor

**Com Axios:**
```javascript
async function deletarFornecedor(id) {
  try {
    const response = await axios.delete(`${API_URL}/fornecedor/${id}`);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

---

## 🔗 VÍNCULOS (Fornecedor ↔ Material)

### Vincular material a fornecedor

**Com Axios:**
```javascript
async function vincularMaterial(idFornecedor, idMaterial) {
  try {
    const response = await axios.post(`${API_URL}/vincularMaterial`, {
      id_fornecedor: idFornecedor,
      id_materiaPrima: idMaterial
    });
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}

// Exemplo
vincularMaterial(1, 1);
```

### Desvincular material de fornecedor

**Com Axios:**
```javascript
async function desvincularMaterial(idFornecedor, idMaterial) {
  try {
    const response = await axios.delete(`${API_URL}/desvincularMaterial`, {
      data: {
        id_fornecedor: idFornecedor,
        id_materiaPrima: idMaterial
      }
    });
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

### Listar materiais de um fornecedor

**Com Axios:**
```javascript
async function listarMateriaisFornecedor(idFornecedor) {
  try {
    const response = await axios.get(`${API_URL}/fornecedor/${idFornecedor}/materiais`);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

### Listar fornecedores de um material

**Com Axios:**
```javascript
async function listarFornecedoresMaterial(idMaterial) {
  try {
    const response = await axios.get(`${API_URL}/material/${idMaterial}/fornecedores`);
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

---

## 🔬 PESQUISA

### Adicionar pesquisa

**Com Axios:**
```javascript
async function adicionarPesquisa(dados) {
  try {
    const response = await axios.post(`${API_URL}/addPesquisa`, {
      nomePesquisa: dados.nome,
      descricao: dados.descricao,
      dataInicio: new Date(dados.dataInicio).toISOString(),
      dataFim: new Date(dados.dataFim).toISOString(),
      idEtapaPesquisa: dados.idEtapa
    });
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}

// Exemplo
adicionarPesquisa({
  nome: "Vacina COVID-19",
  descricao: "Desenvolvimento de vacina",
  dataInicio: "2024-01-01",
  dataFim: "2024-12-31",
  idEtapa: 1
});
```

### Vincular material à pesquisa

**Com Axios:**
```javascript
async function vincularMaterialPesquisa(idPesquisa, idMaterial) {
  try {
    const response = await axios.post(
      `${API_URL}/pesquisa/${idPesquisa}/vincularMaterial`,
      { idMaterial: idMaterial }
    );
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

### Desvincular material da pesquisa

**Com Axios:**
```javascript
async function desvincularMaterialPesquisa(idPesquisa, idMaterial) {
  try {
    const response = await axios.delete(
      `${API_URL}/pesquisa/${idPesquisa}/desvincularMaterial/${idMaterial}`
    );
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}
```

---

## 🏭 PRODUÇÃO

### Adicionar produção

**Com Axios:**
```javascript
async function adicionarProducao(dados) {
  try {
    const response = await axios.post(`${API_URL}/addProducao`, {
      nomeMedicamento: dados.nome,
      descricaoMedicamento: dados.descricao,
      dataInicio: new Date(dados.dataInicio).toISOString(),
      dataFim: new Date(dados.dataFim).toISOString(),
      idStatusProducao: dados.idStatus,
      idPesquisa: dados.idPesquisa
    });
    return response.data;
  } catch (error) {
    console.error('Erro:', error.response?.data || error.message);
  }
}

// Exemplo
adicionarProducao({
  nome: "Vacina XYZ",
  descricao: "Vacina para COVID-19",
  dataInicio: "2024-06-01",
  dataFim: "2024-12-31",
  idStatus: 1,
  idPesquisa: 1
});
```

---

## 🎨 Exemplo Completo - Formulário HTML + JavaScript

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Cadastro de Material</title>
</head>
<body>
  <h1>Cadastro de Matéria-Prima</h1>
  
  <form id="formMaterial">
    <input type="text" id="nome" placeholder="Nome" required><br>
    <input type="text" id="formula" placeholder="Fórmula"><br>
    <input type="number" id="quantidade" placeholder="Quantidade" required><br>
    <input type="text" id="lote" placeholder="Lote"><br>
    <input type="date" id="dataValidade" required><br>
    <button type="submit">Adicionar Material</button>
  </form>

  <h2>Materiais Cadastrados</h2>
  <ul id="listaMateriais"></ul>

  <script>
    const API_URL = 'http://localhost:5000/api';

    // Adicionar material
    document.getElementById('formMaterial').addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const dados = {
        nome: document.getElementById('nome').value,
        formula: document.getElementById('formula').value,
        quantidade: parseInt(document.getElementById('quantidade').value),
        lote: document.getElementById('lote').value,
        data_validade: document.getElementById('dataValidade').value
      };

      try {
        const response = await fetch(`${API_URL}/addMateriaPrima`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(dados)
        });

        const resultado = await response.json();
        
        if (response.ok) {
          alert('Material adicionado com sucesso!');
          listarMateriais(); // Atualiza a lista
          e.target.reset(); // Limpa o formulário
        } else {
          alert('Erro: ' + resultado.erro);
        }
      } catch (error) {
        console.error('Erro:', error);
        alert('Erro ao adicionar material');
      }
    });

    // Listar materiais
    async function listarMateriais() {
      try {
        const response = await fetch(`${API_URL}/materia-prima`);
        const materiais = await response.json();
        
        const lista = document.getElementById('listaMateriais');
        lista.innerHTML = '';
        
        materiais.forEach(material => {
          const li = document.createElement('li');
          li.textContent = `${material.nome} - ${material.formula} - Qtd: ${material.quantidade}`;
          lista.appendChild(li);
        });
      } catch (error) {
        console.error('Erro ao listar materiais:', error);
      }
    }

    // Carrega a lista ao abrir a página
    listarMateriais();
  </script>
</body>
</html>
```

---

## 💡 Dicas Importantes

1. **CORS:** Se você encontrar erros de CORS, certifique-se de que o Flask está configurado para aceitar requisições do frontend:
   ```python
   from flask_cors import CORS
   CORS(app)
   ```

2. **Tratamento de Erros:** Sempre trate erros com try/catch

3. **Validação:** Valide os dados antes de enviar para a API

4. **Encode URLs:** Use `encodeURIComponent()` para nomes com espaços ou caracteres especiais

5. **Datas:** Converta datas para formato ISO com `new Date().toISOString()`

6. **Axios vs Fetch:** Axios é mais simples e já retorna JSON automaticamente

---

## 📚 Recursos Adicionais

- [Fetch API - MDN](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API)
- [Axios Documentation](https://axios-http.com/docs/intro)
- [JavaScript Promises](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Promise)
