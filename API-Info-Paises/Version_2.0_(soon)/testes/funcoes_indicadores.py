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


def show_specific_indicator_of_specific_country(country, indicator):
    country = country
    indicator = indicator

    try:
        request = requests.get(
            f"https://servicodados.ibge.gov.br/api/v1/paises/{country}/indicadores/{indicator}")
        list_of_indicator = json.loads(request.text)

        dict_of_indicator = list_of_indicator[0]

        return dict_of_indicator

    except Exception as ex:
        dict_error = {"xxErrorxx (capture_indicator)": f"{ex}"}

        return dict_error


def show_all_indicators_of_selected_country(country):
    country = country

    try:
        request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/paises/{country}/indicadores/")
        list_indicators_of_source = json.loads(request.text)

        areas_and_subjects_list = list()
        information_of_subject = list()

        for indicator in list_indicators_of_source:
            string_indicador = indicator['indicador']
            parameter = _found_string_position(string_indicador, '-')

            area = string_indicador[0:parameter - 1]
            subject = f"{indicator['id']}:  {string_indicador[parameter + 2:]}"

            try:
                unidade = indicator['unidade']['id']
            except Exception as ex:
                unidade = f"error :{ex}"

            if not indicator['series']:
                pass
            else:
                for information in indicator['series'][0]['serie']:

                    for data in information:
                        if information[data] is None:
                            pass
                        else:
                            string = f"Data({data}): {information[data]} {unidade}"
                            information_of_subject.append(string)

            areas_and_subjects_list.append((area, subject, information_of_subject))

        research_areas = dict()
        the_last_one = ''
        for x, y, z in areas_and_subjects_list:
            var = {y: z}
            if the_last_one != x:
                the_last_one = x
                research_areas[x] = list()

                research_areas[x].append(var)
            else:
                research_areas[x].append(var)

        return research_areas

    except Exception as ex:
        print(ex)


def _found_string_position(string, caractere):
    index = 0
    while index < len(string):
        if string[index] == caractere:
            return index
        index = index + 1

    return -1


"""print(show_indicators_id())
print("--------------")
print(show_specific_indicator_of_specific_country("BR", "77818"))
print("--------------")"""
print(show_all_indicators_of_selected_country("US"))
