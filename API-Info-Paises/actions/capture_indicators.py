import json
import requests


def show_indicators_id():
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/indicadores")
    dict_of_indicators = json.loads(request.text)

    all_indicators_and_ids = dict()
    for i in dict_of_indicators:
        all_indicators_and_ids[f"{i['indicador']}"] = i['id']

    return all_indicators_and_ids


def show_specific_indicator_of_specific_country(country, indicator):
    country = country
    indicator = indicator
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{country}/indicadores/{indicator}")
    dict_of_indicator = json.loads(request.text)

    return dict_of_indicator


def show_all_indicators_of_selected_country(country):
    country = country
    request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{country}/indicadores/")
    dict_of_indicator = json.loads(request.text)

    return dict_of_indicator
