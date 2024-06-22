# Extrator de Dados de Acidentes em BH

## Requirements
Para esse código rodar, os seguintes requisitos são necessários:
- Google Chrome: O script usa Selenium para baixar os dados com o Google Chrome.
- GCP: O script é feito para escrever os dados no BigQuery e, portanto, precisa de uma SA com permissões para escrita.

## How to run
1. Acesse o arquivo ./config/prod.conf e preencha as informações de acordo com o ambiente GCP que você tem. As informações são:
    * **project_id**: Nome do projeto GCP
    * **bucket_name**: Nome do bucket onde os arquivos serão salvos no seu estado bruto
    * **dataset_name**: Dataset do bigquery onde ficará a tabela final
    * **table_name**: Nome da tabela final

2. Importe a variável de ambiente do GCP (Linux only)
    2.1 Abra o terminal
    2.2 Execute o comando: export GOOGLE_APPLICATION_CREDENTIALS=/path/to/sa/sa_name.json

3. Instale as libs
    3.1 No terminal, navegue até a pasta raiz do projeto
    3.2 Se quiser usar algum ambiente virtual, pode criar nesse momento
    3.3 Rode o comando "pip install -r requirements.txt"

4 Rode o script
    4.1 No terminal, navegue até a pasta raiz do projeto
    4.2 Rode o comando "python3 main.py"

## Limitações
Por se tratar de um projeto de demonstração, o projeto possui algumas limitações. As principais:
- Checagem do GCP: O script possui uma exceção para caso o bucket nomeado no início já exista. Entretanto, essa é a única checagem. No geral, o script implementa nenhum tratamento de exceções.
- Processamento dos dados: Nenhum processamento para gerar valor nos dados é feito. Apenas renomeação e organização de colunas para que a tabela final a ser escrita no BigQuery faça sentido.