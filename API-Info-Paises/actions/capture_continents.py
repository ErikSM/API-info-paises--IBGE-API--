import json
import requests


request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
source_dictionary = json.loads(request.text)

region = dict()

for item in source_dictionary:
    region[item['sub-regiao']['regiao']['nome']] = list()

for item in source_dictionary:
    if item['sub-regiao']['regiao']['nome'] == "Ásia":
        region[item['sub-regiao']['regiao']['nome']].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")
    elif item['sub-regiao']['regiao']['nome'] == "África":
        region[item['sub-regiao']['regiao']['nome']].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")
    elif item['sub-regiao']['regiao']['nome'] == "América":
        region[item['sub-regiao']['regiao']['nome']].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")
    elif item['sub-regiao']['regiao']['nome'] == "Europa":
        region[item['sub-regiao']['regiao']['nome']].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")
    elif item['sub-regiao']['regiao']['nome'] == "Oceania":
        region[item['sub-regiao']['regiao']['nome']].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")
    else:
        region[item['sub-regiao']['regiao']['nome']].append(item['nome'])


def show_all_continents():
    continents = list()
    for i in region:
        continents.append(i)
    return continents


def show_contries_each_continent():
    return region


def show_number_of_countries_from_each_continent():
    number_of_contries = dict()
    for i in region:
        number_of_contries[i] = len(region[i])
    return number_of_contries
