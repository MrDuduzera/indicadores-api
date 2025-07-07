# 📊 Indicadores Econômicos — AV3 Programação Servidor

Este é um sistema web desenvolvido como parte da AV3 da disciplina de Programação Servidor.  
Ele permite cadastrar, listar, editar e excluir indicadores econômicos, além de exibir a taxa Selic atual usando a API do Banco Central.

---

## 🔧 Tecnologias utilizadas

- **Django 5.2.4** (com Django REST Framework)
- **HTML + CSS + JavaScript**
- **Fetch API**
- **Render.com** (deploy da API)
- **Banco de dados SQLite3**

---

## 📌 Funcionalidades

- ✅ Listar indicadores (PIB, IPCA, Câmbio, Receita, etc.)
- ✅ Cadastrar novo indicador
- ✅ Editar indicador existente
- ✅ Excluir indicador
- ✅ Exibir taxa Selic (API pública do Banco Central)

---

## 🔗 Links importantes

- 🌐 **API online (Render):**  
  [`https://indicadores-api-t5id.onrender.com/api/indicadores/`](https://indicadores-api-t5id.onrender.com/api/indicadores/)

- 📄 **API de Taxa Selic (Banco Central):**  
  [`https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json`](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json)

---

## 🖼️ Prints do sistema

> (Você pode adicionar prints do `index.html` funcionando aqui, se quiser)

---

## 💻 Como rodar o projeto localmente

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/indicadores-api.git
