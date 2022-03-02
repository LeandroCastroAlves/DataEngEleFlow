import os
import pandas as pd

pasta = 'arquivosTeste/AIR_CIA'
NumPasta = []

def EtlAnac():
#Loop para pegar os arquivos no diretorio
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            NumPasta.append(arquivo)
            print(os.path.join(diretorio, arquivo))
            arquivoLocal = os.path.join(diretorio, arquivo)
            arquivo = arquivoLocal
            arquivo_ = arquivo.split('\\')[1]
            print(arquivo_)

            #Colocando os nomes das colunas em modo snake case
            dados = pd.read_csv(arquivo, names=['Razao_Social','ICAO_IATA', 'CNPJ','Atividades_Aereas','Endereco_Sede','Telefone','E_Mail',
                                         'Decisao_Operacional','Data_Decisao_Operacional','Validade_Operacional'], sep=';')

            #Tirando primeira llinha
            dados=dados.drop(dados.index[[0]])

            #Separando a coluna em duas
            novaColuna = dados["ICAO_IATA"].str.split(" ", n=1, expand=True)

            #Criando coluna ICAO
            dados["ICAO"]= novaColuna[0]

            # Criando coluna IATA
            try:
                dados["IATA"] = novaColuna[1]
            except:
                dados["IATA"] = 'NULL'

            # Retirando coluna
            dados.drop(columns=["ICAO_IATA"], inplace=True)

            # Salvando arquivo full com todos os CSVs
            dados.to_csv('arquivosModificados/AIR_CIA/AnacFull.csv', index=False, sep=';', mode='a')

EtlAnac()




















