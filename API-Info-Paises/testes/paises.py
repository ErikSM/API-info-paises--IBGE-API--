import json
import requests


def mostrar_conteudo_de_pais_especifico(pais):
    request = requests.get(f""
                           f"https://servicodados.ibge.gov.br/api/v1/paises/"
                           f"{pais}"
                           )

    lista_com_dicionario_do_pais = json.loads(request.text)

    for i in lista_com_dicionario_do_pais[0]:
        print(i)
