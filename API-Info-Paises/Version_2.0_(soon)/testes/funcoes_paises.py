import json
import requests

from objects.Country import Country

todos_os_paises = dict()

try:
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
    all_world_in_source = json.loads(request.text)
    for item in all_world_in_source:

        code_id = item['id']
        name = item['nome']
        country = Country(code_id, name)

        country.location['continente'] = item['sub-regiao']['regiao']['nome']
        country.location['regiao'] = item['sub-regiao']['nome']

        if item['regiao-intermediaria'] is None:
            country.location['regiao especifica'] = "---"
        else:
            country.location['regiao especifica'] = item['regiao-intermediaria']['nome']

        todos_os_paises[country.name] = country

except Exception as ex:
    print(ex)


def mostrar_informacoes_completas_sobre_paises():
    try:

        for i in todos_os_paises:
            specific_request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/"
                                            f"{i.code_id['ISO-ALPHA-2']}")
            specific_world_in_source = json.loads(specific_request.text)

            i.area = specific_world_in_source[0]['area']
            i.languages = specific_world_in_source[0]['linguas']
            i.government = specific_world_in_source[0]['governo']
            i.currency_units = specific_world_in_source[0]['unidades-monetarias']
            i.historic = specific_world_in_source[0]['historico']

    except Exception as ex_2:
        print(ex_2)


def mostrar_informacoes_de_pais_especifico(pais):
    try:
        specific_request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{pais}")
        specific_world_in_source = json.loads(specific_request.text)

        id_country = specific_world_in_source[0]['id']['ISO-3166-1-ALPHA-2']
        name_country = specific_world_in_source[0]['nome']['abreviado']

        country_object = Country(id_country, name_country)

        country_object.location = specific_world_in_source[0]['localizacao']
        country_object.area = specific_world_in_source[0]['area']
        country_object.languages = specific_world_in_source[0]['linguas']
        country_object.government = specific_world_in_source[0]['governo']
        country_object.currency_units = specific_world_in_source[0]['unidades-monetarias']
        country_object.historic = specific_world_in_source[0]['historico']

        return country_object

    except Exception as ex_3:
        print(ex_3)


teste = mostrar_informacoes_de_pais_especifico('BR')

print(teste.show_all_informaton_about())
