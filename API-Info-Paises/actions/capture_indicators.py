import json
import requests


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


def show_specific_indicator_of_specific_country(country, indicator):
    country = country
    indicator = indicator

    try:
        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{country}/indicadores/{indicator}")
        dict_of_indicator = json.loads(request.text)

        return dict_of_indicator

    except Exception as ex:
        dict_error = {"xxErrorxx (capture_indicator)": f"{ex}"}

        lista_error = list()
        lista_error.append(dict_error)

        return lista_error


def show_all_indicators_of_selected_country(country):
    country = country

    try:
        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{country}/indicadores/")
        dict_of_indicator = json.loads(request.text)

        return dict_of_indicator

    except Exception as ex:
        print(ex)
