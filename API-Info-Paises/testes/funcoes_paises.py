import json
import requests

from ObjetoPais import *


def mostrar_conteudo_de_pais_especifico(pais):
    request = requests.get(f""
                           f"https://servicodados.ibge.gov.br/api/v1/paises/"
                           f"{pais}"
                           )

    lista_com_dicionario_do_pais = json.loads(request.text)

    for i in lista_com_dicionario_do_pais[0]:
        print(i)


def mostrar_todos_os_paises_existentes():
    request = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/paises")

    lista_com_dicionario_do_pais = json.loads(request.text)

    for i in lista_com_dicionario_do_pais:
        print(i)
        print(f"{'-' * 20}")
        if '{"id":{"M49":76,"ISO-3166-1-ALPHA-2":"BR","ISO-3166-1-ALPHA-3":"BRA"}' in i:

            print(i)
            print(f"{'-'*20}")


def criar_objeto_pais_add_em_lista():
    request = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/paises")

    lista_com_dicionario_do_pais = json.loads(request.text)

    lista_paises = list()
    for i in lista_com_dicionario_do_pais:
        pais = ObjetoPais(i["id"]["ISO-ALPHA-2"], i["nome"])
        lista_paises.append(pais)

    for i in lista_paises:
        print(i.code_id)
        print(i.name)
        print(f"{'-' * 20}")


criar_objeto_pais_add_em_lista()
