import os
import json
import pandas as pd

VraFull = []
list(VraFull)
def EtlVra():
    global VraFull
    pasta = 'arquivosTeste/VRA'
    NumPasta = []
    ListaIcao = []

    # Listando arquivos no diretorio
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            NumPasta.append(arquivo)
            arquivoLocal = os.path.join(diretorio, arquivo)
            print('Lendo os arquivo')
            # Lendo os arquivos
            with open(arquivoLocal, 'r', encoding='utf-8-sig') as f:
                conteudo = f.read()

            x = conteudo.replace('é', 'e').replace('ó', 'o').replace('ç', 'c').replace('ã', 'a').replace('ú', 'u')
            dados = json.loads(x)
            print('Normalizando o cabeçalho para snake case')
            # Normalizando o cabeçalho para snake case
            for i in range(len(dados)):
                df = dados[i]
                df["icao_empresa_aerea"] = df.pop("ICAOEmpresaAerea")
                df["numero_voo"] = df.pop("NumeroVoo")
                df["codigo_autorizacao"] = df.pop("CodigoAutorizacao")
                df["codigo_tipo_linha"] = df.pop("CodigoTipoLinha")
                df["icao_aerodromo_origem"] = df.pop("ICAOAerodromoOrigem")
                df["icao_aerodromo_destino"] = df.pop("ICAOAerodromoDestino")
                df["partida_prevista"] = df.pop("PartidaPrevista")
                df["partida_real"] = df.pop("PartidaReal")
                df["chegada_prevista"] = df.pop("ChegadaPrevista")
                df["chegada_real"] = df.pop("ChegadaReal")
                df["situacao_voo"] = df.pop("SituacaoVoo")
                df["codigo_justificativa"] = df.pop("CodigoJustificativa")

            print('Somando Listas')
            # Juntando os json para tem um arquivo apenas
            VraFull = (VraFull + dados)
    print('Salvando Json Full em arquivosModificados/VRA/VraFull.json')
    # Salvando arquivo VRA
    with open('arquivosModificados/VRA/VraFull.json ', 'w') as fp:
        json.dump(VraFull, fp)

    print('Criando lista icao')
    # Criando lista de ICAO
    for i in range(len(VraFull)):
        df = VraFull[i]
        icaoe = df["icao_empresa_aerea"]
        icaod = df["icao_aerodromo_destino"]
        icaoo = df["icao_aerodromo_origem"]
        ListaIcao.append(icaoe)
        ListaIcao.append(icaod)
        ListaIcao.append(icaoo)

    listaIcao = pd.DataFrame(ListaIcao)
    print('salvando')
    # Salvando lista de ICAOs
    listaIcao.to_csv('C:\desafioDataEngEleFlow/arquivosModificados\LISTA_ICAO\lista.csv', index=False, sep=';')

EtlVra()












































