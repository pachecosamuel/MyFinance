# Explicação da arquitetura

#### src/domain: Contém as entidades e os casos de uso, representando o core do seu negócio.
<hr>

#### src/infrastructure: Contém os adaptadores e drivers para interagir com o mundo externo, como bancos de dados, serviços externos, etc.
<hr>

#### src/application: Contém a lógica de aplicação, que orquestra os casos de uso e as interfaces.
<hr>

# Execução básica do código
#### poetry run python src/app/interfaces/api.py

<hr>

<br><br><br>


# Gerenciamento de Scripts e Tarefas


### Lista os scripts definidos no arquivo pyproject.toml (na seção [tool.poetry.scripts]).
poetry run list

### Executa um script definido no pyproject.toml.
poetry run <script>



# Gerenciamento do Projeto


# Exibe informações sobre o projeto atual (nome, versão, dependências, etc.).
poetry about

# Verifica por atualizações disponíveis do Poetry.
poetry self update

# Publica o pacote em um repositório (como o PyPI).
poetry publish --build


### Configurações Importantes


### Se o arquivo de configuração 'alembic.ini' precisar ser editado para incluir a string de conexão ao banco:
### Exemplo de configuração para SQLite (substitua driver://user:pass@host/dbname pelo seu caso):
sqlalchemy.url = sqlite:///src/database/app.db
### Ou PostgreSQL:
sqlalchemy.url = postgresql://username:password@localhost/database_name

### ========================
### Dicas de Uso
### ========================

### 1. Revise sempre os arquivos gerados automaticamente em "migrations/versions".
### 2. Realize testes locais antes de aplicar migrações em produção.
### 3. Use comentários claros nas mensagens das migrações (-m) para facilitar a identificação no histórico.
### 4. Para colaboração em equipe, sincronize as migrações no repositório (Git).
### 5. Evite editar migrações que já foram aplicadas em produção.


<hr>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
project_root/
├── .gitignore
├── LICENSE
├── README.md
├── myenv/                  # Ambiente virtual (não será versionado pelo Git)
├── pyproject.toml          # Gerenciado pelo Poetry
├── src/                    # Todo o código-fonte do projeto
│   ├── app/                # Módulo principal do aplicativo
│   │   ├── __init__.py
│   │   ├── domain/         # Entidades da aplicação
│   │   │   ├── __init__.py
│   │   │   └── models.py   # Modelos de domínio
│   │   ├── application/    # Casos de uso e regras de negócio
│   │   │   ├── __init__.py
│   │   │   └── use_cases.py
│   │   ├── infrastructure/ # Conexão com recursos externos (DB, APIs)
│   │   │   ├── __init__.py
│   │   │   └── orm.py      # Configuração do ORM
│   │   ├── interfaces/     # Interfaces (ex.: REST APIs, CLI)
│   │   │   ├── __init__.py
│   │   │   └── api.py
│   ├── tests/              # Testes unitários e de integração
│       ├── __init__.py
│       └── test_sample.py
