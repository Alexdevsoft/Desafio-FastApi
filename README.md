# Store API

Este repositório contém a implementação de uma API de produtos utilizando FastAPI, MongoDB e Pytest para testes.

**Uma API RESTful para gerenciamento de produtos.**

## Estrutura do Projeto

- **store**

  - **core**
    - `config.py`: Configurações principais do projeto.
  - **db**
    - `mongo.py`: Cliente MongoDB para acesso ao banco de dados.
  - **routers**
    - `api_router.py`: Definição das rotas da API.
  - **schemas**
    - `product.py`: Esquemas Pydantic para validação e definição de produtos.
  - **usecases**
    - `product.py`: Casos de uso para operações de produto.

- **tests**
  - `factories.py`: Fábrica de dados para testes.
  - `test_product.py`: Testes para o módulo de produtos.
 
  **Criar Produto:** O caso de uso "criar produto" valida os dados do produto, cria um novo documento no MongoDB e retorna o produto criado.


## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu-usuario/store-api.git
   cd store-api
   ```

2. Crie um ambiente virtual e ative-o:

   ```sh
   python -m venv env
   source env/bin/activate  # No Windows use `env\Scripts\activate`
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Configure o banco de dados no arquivo de configuração `store/core/config.py`.

## Execução

Para iniciar a aplicação FastAPI, execute:

```sh
uvicorn store.main:app --reload
```
