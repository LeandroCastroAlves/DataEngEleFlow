<img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>

# Data engineering capstone

## BigData Airlines

A Eleflow irá atender um novo cliente, a _BigData Airlines_, e você será o engenheiro de dados responsável por fazer a ingestão de dados e preparar algumas tabelas para os cientistas de dados e analistas de dados. 

### Capstone

- Carregar os dados de VRA
  - Normalizar o cabeçalho para snake case
  - Salvar estes dados
- Carregar dos dados de AIR_CIA
  - Normalizar o cabeçalho para snake case
  - Separar a coluna 'ICAO IATA' em duas colunas, seu conteúdo está separado por espaço e pode não conter o código IATA, caso não contenha o código IATA, deixe o valor nulo.
  - Salvar estes dados
- Criar nova tabela aerodromos
  - Através da API [https://rapidapi.com/Active-api/api/airport-info/]() trazer os aeródramos através do código ICAO presente nos dados de VRA.
  - Salvar estes dados
- Criar as seguintes views (Priorize o uso de SQL para esta parte):
  - Para cada companhia aérea trazer a rota mais utilizada com as seguintes informações:
    - Razão social da companhia aérea
    - Nome Aeroporto de Origem
    - ICAO do aeroporto de origem
    - Estado/UF do aeroporto de origem
    - Nome do Aeroporto de Destino
    - ICAO do Aeroporto de destino
    - Estado/UF do aeroporto de destino
  - Para cada aeroporto trazer a companhia aérea com maior atuação no ano com as seguintes informações:
    - Nome do Aeroporto
    - ICAO do Aeroporto
    - Razão social da Companhia Aérea
    - Quantidade de Rotas à partir daquele aeroporto
    - Quantidade de Rotas com destino àquele aeroporto
    - Quantidade total de pousos e decolagens naquele aeroporto

#### Extras:
  - Descrever qual estratégia você usaria para ingerir estes dados de forma incremental caso precise capturar esses dados a cada mes?
  - Justifique em cada etapa sobre a escalabilidade da tecnologia utilizada.
  - Justifique as camadas utilizadas durante o processo de ingestão até a disponibilização dos dados.

#### Observações:
   - Você pode utilizar a tecnologia de sua preferência ou seguir a recomendação:
     - Notebooks Jupyter
     - Google Colab
     - Databricks Community
   - Pode incluir comentários sobre a abordagem de extração/transformação que você está fazendo
   - Pode disponibilizar o projeto via Git, URL ou .zip

# desafioDataEngEleFlow
Repositorio para desafio EleFlow

Prezados,

Segue link HTML do notebook do Databricks:
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3953060251362654/3696436976097108/4249033897394522/latest.html

As ETL tem comentarios sobre os processos que fiz.

---------------------------------------------

- Descrever qual estratégia você usaria para ingerir estes dados de forma incremental caso precise capturar esses dados a cada mes?



Eu faria um job escredulado que rodasse a cada mes quando os arquivos chegassem em uma pasta ou qualquer lugar que seja, e para evitar erros eu colocaria uma chave unica como coluna, neste caso, um checksum de todas as colunas, então faria um upsert ou algo parecido, e se houver algum dado repetido, os registros não duplicariam. Os novos arquivos seriam mesclados com o arquivo full já consistente, só inserindo dados em que não existam no arquivo.


- Justifique em cada etapa sobre a escalabilidade da tecnologia utilizada.


Juntei os arquivos em um só para que se houver uma frequência grande de arquivos sempre mesclariam e não ficaríamos com inúmeros arquivos. No databrick, onde os dados foram salvos e pode-se executar as ETLs, possui a possibilidade de se escrever em linguagens como Python, Scala SQL e R nos dando o poder de escolhe qual mais necessitamos para um processo. Com a quantidade de dados aumentando e a necessidade de processamento de dados, o Databricks oferece a possibilidade de escalar clusters, resolvendo problemas de processamento de dados.


- Justifique as camadas utilizadas durante o processo de ingestão até a disponibilização dos dados.


Na extração dos dados, os scripts python são responsáveis pela extração dos dados, pois é extremamente fácil e rápido fazer este processo com a linguagem python. Ainda com o python, é feita a transformação destes dados, como alterações de colunas, divisão de colunas e o que quer que necessite, usando pandas pela facilidade de manipulação. Os dados são salvos também com scripts python. Com os dados já transformados e prontos para serem consumidos, as queries SQL rodam e disponibilizam as informações no databricks, que junto com o Apache Spark fornece um desempenho de processamento de dados muito relevante.
