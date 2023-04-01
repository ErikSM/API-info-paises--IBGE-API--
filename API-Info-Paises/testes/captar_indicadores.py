import json
import requests


def mostrar_id_dos_indicadores():
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/indicadores")
    dicionario = json.loads(request.text)
    for i in dicionario:
        print(f"*({i['id']}):  {i['indicador']}")


def mostrar_indicadores(pais, id):
    pais = pais
    indicador = id
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{pais}/indicadores/{indicador}")
    dicionario_do_indicador = json.loads(request.text)

    for i in dicionario_do_indicador[0]:
        print(f'**{i}')
        print(dicionario_do_indicador[0][i])


def mostrar_todos_os_indicadores_de_um_pais(pais):
    pais = pais
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{pais}/indicadores/")
    dicionario_de_indicador = json.loads(request.text)

    for i in dicionario_de_indicador:
        print(f"{i['indicador']}: \n{i['series'][0]}")


mostrar_id_dos_indicadores()
print(f"\n{'-'*20}\n")
mostrar_indicadores('US', '77849')
print(f"\n//{'-'*20}\n")
mostrar_todos_os_indicadores_de_um_pais("BR")