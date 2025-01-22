# Explicação da arquitetura

#### src/domain: Contém as entidades e os casos de uso, representando o core do seu negócio.
<hr>

#### src/infrastructure: Contém os adaptadores e drivers para interagir com o mundo externo, como bancos de dados, serviços externos, etc.
<hr>

#### src/application: Contém a lógica de aplicação, que orquestra os casos de uso e as interfaces.
<hr>

# Execução básica do código
#### poetry run python src/app/interfaces/api.py

<br><br><br><br>

# Comandos Básicos do Alembic


### Inicializa o Alembic no projeto, criando a estrutura básica de diretórios e arquivos.
alembic init migrations

### Cria uma nova migração vazia para adicionar manualmente alterações no banco de dados.
alembic revision -m "Descrição da migração"

### Gera automaticamente uma migração com base nas diferenças entre os modelos e o banco de dados.
alembic revision --autogenerate -m "Descrição da migração"

### Aplica todas as migrações pendentes ao banco de dados.
alembic upgrade head

### Aplica uma migração específica, substituindo <revision_id> pelo ID da migração.
alembic upgrade <revision_id>

### Reverte a última migração aplicada.
alembic downgrade -1

### Reverte para uma migração específica, substituindo <revision_id> pelo ID da migração.
alembic downgrade <revision_id>

### Lista o histórico de migrações aplicadas ou disponíveis.
alembic history

### Exibe o ID da migração atualmente aplicada no banco de dados.
alembic current

### Exibe as diferenças detectadas entre os modelos e o banco de dados.
### Útil para revisar antes de criar uma migração.
alembic heads

<br><br>

<br><br><br><br>

# Comandos Básicos do Poetry


## Inicializa um novo projeto Poetry no diretório atual.
poetry init
<br>

## Cria um novo projeto com um layout padrão em um diretório específico.
poetry new my_project
<br>

## Instala todas as dependências listadas no arquivo pyproject.toml.
poetry install
<br>

## Adiciona uma nova dependência ao projeto.
## Substitua <package> pelo nome do pacote desejado.
poetry add <package>
<br>

## Adiciona uma dependência de desenvolvimento.
## Use para ferramentas como linters ou frameworks de teste.
poetry add --dev <package>
<br>

## Remove uma dependência do projeto.
poetry remove <package>
<br>

## Atualiza todas as dependências para suas versões mais recentes.
poetry update
<br>

## Atualiza uma dependência específica.
poetry update <package>
<br>

## Exibe informações sobre as dependências do projeto e suas versões.
poetry show
<br>

## Exibe informações detalhadas sobre uma dependência específica.
poetry show <package>
<br>

## Executa comandos dentro do ambiente virtual gerenciado pelo Poetry.
## Exemplo: poetry run python script.py
poetry run <comando>'
<br>

<br><br>

# Gerenciamento do Ambiente Virtual


### Cria o ambiente virtual, caso ainda não exista.
poetry env use python

### Exibe informações sobre o ambiente virtual ativo.
poetry env info

### Remove o ambiente virtual gerenciado pelo Poetry.
poetry env remove python

<br><br>