import json
import requests


def mostrar_id_dos_indicadores():
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/indicadores")
    dicionario = json.loads(request.text)
    for i in dicionario:
        print(f"*{i['id']}")
        print(i['indicador'])


def mostrar_indicadores(pais, id):
    pais = pais
    indicador = id
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{pais}/indicadores/{indicador}")
    dicionario_do_indicador = json.loads(request.text)

    for i in dicionario_do_indicador[0]:
        print(f'**{i}')
        print(dicionario_do_indicador[0][i])


mostrar_id_dos_indicadores()
print(f"\n{'-'*20}\n")
mostrar_indicadores('US', '77849')
