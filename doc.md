# Explicação da arquitetura

#### src/domain: Contém as entidades e os casos de uso, representando o core do seu negócio.
<hr>

#### src/infrastructure: Contém os adaptadores e drivers para interagir com o mundo externo, como bancos de dados, serviços externos, etc.
<hr>

#### src/application: Contém a lógica de aplicação, que orquestra os casos de uso e as interfaces.
<hr>

# Execução básica do código
#### poetry run python src/app/interfaces/api.py

