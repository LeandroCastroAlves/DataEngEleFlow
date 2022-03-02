# desafioDataEngEleFlow
Repositorio para desafio EleFlow

Prezados,

Segue link HTML do notebook do Databricks:
https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3953060251362654/3696436976097108/4249033897394522/latest.html

As ETL tem comentarios sobre os processos que fiz.

---------------------------------------------

- Descrever qual estratégia você usaria para ingerir estes dados de forma incremental caso precise capturar esses dados a cada mes?



Eu faria um job escredulado a cada início do mes quando os arquivos chegassem em uma pasta ou qualquer lugar que seja, e para evitar erros eu colocaria uma chave unica como coluna, neste caso, um checksum de todas as colunas, então faria um upsert ou algo parecido, e se houver algum dado repetido, os registros não duplicariam. Os novos arquivos seriam mesclados com o arquivo full já consistente, só inserindo dados em que não existam no arquivo.


- Justifique em cada etapa sobre a escalabilidade da tecnologia utilizada.


Juntei os arquivos em um só para que se houver uma frequência grande de arquivos sempre mesclariam e não ficaríamos com inúmeros arquivos. No databrick, onde os dados foram salvos e pode-se executar as ETLs, possui a possibilidade de se escrever em linguagens como Python, Scala SQL e R nos dando o poder de escolhe qual mais necessitamos para um processo. Com a quantidade de dados aumentando e a necessidade de processamento de dados, o Databricks oferece a possibilidade de escalar clusters, resolvendo problemas de processamento de dados.


- Justifique as camadas utilizadas durante o processo de ingestão até a disponibilização dos dados.


Na extração dos dados, os scripts python são responsáveis pela extração dos dados, pois é extremamente fácil e rápido fazer este processo com a linguagem python. Ainda com o python, é feita a transformação destes dados, como alterações de colunas, divisão de colunas e o que quer que necessite, usando pandas pela facilidade de manipulação. Os dados são salvos também com scripts python. Com os dados já transformados e prontos para serem consumidos, as queries SQL rodam e disponibilizam as informações no databricks, que junto com o Apache Spark fornece um desempenho de processamento de dados muito relevante.
