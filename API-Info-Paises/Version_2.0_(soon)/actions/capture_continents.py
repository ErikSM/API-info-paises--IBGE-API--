import json
import requests

from objects.Country import Country

africa = dict()
oceania = dict()
america = dict()
asia = dict()
europa = dict()

all_world_locations = {'Oceania': oceania, 'Europa': europa, 'América': america,
                       'Ásia': asia, 'África': africa}

all_regions_of_the_each_continent = dict()
all_countries_of_the_each_region = dict()

try:
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
    all_countries_from_source_dict = json.loads(request.text)

    for item in all_countries_from_source_dict:
        all_regions_of_the_each_continent[item['sub-regiao']['regiao']['nome']] = set()
        all_countries_of_the_each_region[item['sub-regiao']['nome']] = set()

    for item in all_countries_from_source_dict:

        region = item['sub-regiao']['nome']
        all_regions_of_the_each_continent[item['sub-regiao']['regiao']['nome']].add(region)

        #  ---------------------------------------------------------------------------------------
        code_id = item['id']
        name = item['nome']
        country = Country(code_id, name)

        country.location['continente'] = item['sub-regiao']['regiao']['nome']
        country.location['regiao'] = item['sub-regiao']['nome']

        if item['regiao-intermediaria'] is None:
            country.location['regiao especifica'] = "---"
        else:
            country.location['regiao especifica'] = item['regiao-intermediaria']['nome']
        #  -----------------------------------------------------------------------------------------

        all_countries_of_the_each_region[item['sub-regiao']['nome']].add(country)

    for region_name in all_countries_of_the_each_region:

        if region_name in all_regions_of_the_each_continent['África']:
            africa[region_name] = all_countries_of_the_each_region[region_name]

        elif region_name in all_regions_of_the_each_continent['Ásia']:
            asia[region_name] = all_countries_of_the_each_region[region_name]

        elif region_name in all_regions_of_the_each_continent['América']:
            america[region_name] = all_countries_of_the_each_region[region_name]

        elif region_name in all_regions_of_the_each_continent['Europa']:
            europa[region_name] = all_countries_of_the_each_region[region_name]

        elif region_name in all_regions_of_the_each_continent['Oceania']:
            oceania[region_name] = all_countries_of_the_each_region[region_name]

except Exception as ex:
    for i in all_world_locations:
        all_world_locations[i] = f"  xxErrorxx[capture_continents.py]: \n\n{ex}"


def show_continents():
    lista_temporaria_1 = list()
    for cont in all_world_locations:
        lista_temporaria_1.append(cont)

    return lista_temporaria_1


def show_regions_from_selected_continent(continent):
    lista_temporaria_2 = list()
    for reg in all_world_locations[continent]:
        lista_temporaria_2.append(reg)

    return lista_temporaria_2


def show_countries_from_selected_region(cont, region_of_cont):
    lista_temporaria_3 = list()
    for ctry in all_world_locations[cont][region_of_cont]:
        lista_temporaria_3.append(ctry.name)

    return lista_temporaria_3

'''show_continents()
show_regions_from_selected_continent("Europa")
show_countries_from_selected_region("Europa", "Europa meridional  (Sul da Europa)")'''
