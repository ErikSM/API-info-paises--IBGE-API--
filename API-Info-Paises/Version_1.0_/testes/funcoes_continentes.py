import json
import requests


request = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises")
dicionario_fonte = json.loads(request.text)

regioes = dict()

for iten in dicionario_fonte:
    regioes[iten['sub-regiao']['regiao']['nome']] = list()

for iten in dicionario_fonte:
    if iten['sub-regiao']['regiao']['nome'] == "Ásia":
        regioes[iten['sub-regiao']['regiao']['nome']].append(iten['nome'])
    elif iten['sub-regiao']['regiao']['nome'] == "África":
        regioes[iten['sub-regiao']['regiao']['nome']].append(iten['nome'])
    elif iten['sub-regiao']['regiao']['nome'] == "América":
        regioes[iten['sub-regiao']['regiao']['nome']].append(iten['nome'])
    elif iten['sub-regiao']['regiao']['nome'] == "Europa":
        regioes[iten['sub-regiao']['regiao']['nome']].append(iten['nome'])
    elif iten['sub-regiao']['regiao']['nome'] == "Oceania":
        regioes[iten['sub-regiao']['regiao']['nome']].append(iten['nome'])
    else:
        regioes[iten['sub-regiao']['regiao']['nome']].append(iten['nome'])


def mostrar_continentes_existentes():
    continentes = list()
    for i in regioes:
        continentes.append(i)
    return continentes


def mostrar_paises_de_cada_continente():
    """print(regioes)
    for iten in regioes:
        print(iten)
        print(regioes[iten])"""
    return regioes


def mostrar_numero_de_paises_de_cada_continente():
    dicionario_temporario = dict()
    for i in regioes:
        dicionario_temporario[i] = len(regioes[i])
    # print(dicionario_temporario)
    return dicionario_temporario

    # graphics.lines_graphic_ramp_up(dicionario_temporario, "Continentes", "No de paises", "Paises por Continentes")
    # graphics.bars_graphic_ramp_up(dicionario_temporario, "Continentes", "No de paises", "Paises por Continente")


print(mostrar_paises_de_cada_continente())
print("--------------------------")
print(mostrar_numero_de_paises_de_cada_continente())
print("-------------------------")
print(mostrar_continentes_existentes())