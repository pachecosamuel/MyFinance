# Explicação da arquitetura

#### src/domain: Contém as entidades e os casos de uso, representando o core do seu negócio.
<hr>

#### src/infrastructure: Contém os adaptadores e drivers para interagir com o mundo externo, como bancos de dados, serviços externos, etc.
<hr>

#### src/application: Contém a lógica de aplicação, que orquestra os casos de uso e as interfaces.
<hr>

# Execução básica do código
#### poetry run python src/app/interfaces/api.py


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
