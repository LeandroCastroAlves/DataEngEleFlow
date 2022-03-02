import requests
import json
import pandas as pd

#Autenticação API
url = "https://airport-info.p.rapidapi.com/airport"
headers = {
    'x-rapidapi-host': "airport-info.p.rapidapi.com",
    'x-rapidapi-key': "e006a0248amshf6f7e049422c0f3p1a49c3jsnb18772007f0a"
}

ListaSemDuplicado = []
ListaFUll = []
lista = pd.read_csv('arquivosModificados/LISTA_ICAO/lista.csv')

def EtlApi():

    # Pegando lista de ICAOs e removendo ICAOs duplicados
    for i in lista:
        ListaFUll.append(lista[i].values)
    listaDuplicado = ListaFUll[0]
    for element in list(listaDuplicado):
        if element not in ListaSemDuplicado:
            ListaSemDuplicado.append(element)

    # Pegando dados da API
    ListaCompleta = []
    for i in range(len(ListaSemDuplicado)):
        querystring = {"icao": ListaSemDuplicado[i]}
        response = requests.request("GET", url, headers=headers, params=querystring)
        dados = json.loads(response.text)
        try:
            print(dados['icao'])
            ListaCompleta.append(dados)
        except:
            x = 1

    # Salvando dados da API no arquivo aerodromos
    with open('arquivosModificados/API_AERODROMOS/aerodromos.json', 'w', encoding='utf-8-sig') as fp:
        json.dump(ListaCompleta, fp)

EtlApi()


