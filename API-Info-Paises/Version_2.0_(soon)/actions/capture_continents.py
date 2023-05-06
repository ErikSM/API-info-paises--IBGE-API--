import json
import requests

all_contries_of_the_each_continent = dict()
regions_of_the_each_continent = dict()


try:

    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
    all_world_contries_dict = json.loads(request.text)

    for item in all_world_contries_dict:
        all_contries_of_the_each_continent[item['sub-regiao']['regiao']['nome']] = list()
        regions_of_the_each_continent[item['sub-regiao']['regiao']['nome']] = list()

    for item in all_world_contries_dict:
        if item['sub-regiao']['regiao']['nome'] == "Ásia":

            all_contries_of_the_each_continent["Ásia"].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")

            if item['sub-regiao']['nome'] not in regions_of_the_each_continent["Ásia"]:
                regions_of_the_each_continent["Ásia"].append(item['sub-regiao']['nome'])

        elif item['sub-regiao']['regiao']['nome'] == "África":

            all_contries_of_the_each_continent["África"].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")

            if item['sub-regiao']['nome'] not in regions_of_the_each_continent["África"]:
                regions_of_the_each_continent["África"].append(item['sub-regiao']['nome'])

        elif item['sub-regiao']['regiao']['nome'] == "América":

            all_contries_of_the_each_continent["América"].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")

            if item['sub-regiao']['nome'] not in regions_of_the_each_continent["América"]:
                regions_of_the_each_continent["América"].append(item['sub-regiao']['nome'])

        elif item['sub-regiao']['regiao']['nome'] == "Europa":

            all_contries_of_the_each_continent["Europa"].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")

            if item['sub-regiao']['nome'] not in regions_of_the_each_continent["Europa"]:
                regions_of_the_each_continent["Europa"].append(item['sub-regiao']['nome'])

        elif item['sub-regiao']['regiao']['nome'] == "Oceania":

            all_contries_of_the_each_continent["Oceania"].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")

            if item['sub-regiao']['nome'] not in regions_of_the_each_continent["Oceania"]:
                regions_of_the_each_continent["Oceania"].append(item['sub-regiao']['nome'])

        else:
            name_temporary = f"{item['sub-regiao']['regiao']['nome']}"
            all_contries_of_the_each_continent[name_temporary].append(f"{item['id']['ISO-ALPHA-2']}: {item['nome']}")

            if item['sub-regiao']['nome'] not in regions_of_the_each_continent[name_temporary]:
                regions_of_the_each_continent[name_temporary].append(item['sub-regiao']['nome'])

except Exception as ex:

    all_contries_of_the_each_continent["xxError (capture_continents)"] = [f"{ex}"]


def show_all_contries_of_the_each_continent():
    return all_contries_of_the_each_continent


def show_regions_of_the_each_continent():
    return regions_of_the_each_continent


def show_all_continents():
    continents = list()
    for continent in all_contries_of_the_each_continent:
        continents.append(continent)

    return continents


def show_number_of_countries_from_each_continent():
    number_of_contries = dict()
    for i in all_contries_of_the_each_continent:
        number_of_contries[i] = len(all_contries_of_the_each_continent[i])
    return number_of_contries


print(show_all_contries_of_the_each_continent())
print(show_regions_of_the_each_continent())
