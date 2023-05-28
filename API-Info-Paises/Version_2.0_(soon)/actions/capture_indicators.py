import json
import requests

from objects.Country import Country


def show_indicators_id():
    try:
        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/indicadores")
        dict_of_indicators = json.loads(request.text)

        all_indicators_and_ids = dict()
        for i in dict_of_indicators:
            all_indicators_and_ids[f"{i['indicador']}"] = i['id']

        return all_indicators_and_ids

    except Exception as ex:
        error_dict = dict()
        error_dict[f"xxErrorxx(capture_indicators)"] = f"{ex}"

        return error_dict


def show_specific_indicator_of_specific_country(country: Country, indicator):
    country = country
    indicator = indicator

    try:
        request = requests.get(
            f"https://servicodados.ibge.gov.br/api/v1/paises/{country.code_id}/indicadores/{indicator}")
        list_of_indicator = json.loads(request.text)

        dict_of_indicator = list_of_indicator

        return dict_of_indicator

    except Exception as ex:
        dict_error = {"xxErrorxx (capture_indicator)": f"{ex}"}

        return dict_error


def show_all_indicators_of_selected_country(country: Country):
    country = country

    try:
        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{country.code_id}/indicadores/")
        dict_of_indicator = json.loads(request.text)

        return dict_of_indicator



    except Exception as ex:
        print(ex)


'''print(show_indicators_id())
print("--------------")
print(show_all_indicators_of_selected_country("US"))
print("--------------")
print(show_specific_indicator_of_specific_country("BR", "77818"))'''
