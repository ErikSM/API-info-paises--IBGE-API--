import json
import requests
from graficos import graficos

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


def mostrar_paises_de_cada_continente():
    print(regioes)
    for iten in regioes:
        print(iten)
        print(regioes[iten])


def mostrar_numero_de_paises_de_cada_continente():
    dicionario_teste = dict()
    for i in regioes:
        dicionario_teste[i] = len(regioes[i])
    print(dicionario_teste)

    graficos.lines_graphic_ramp_up(dicionario_teste, "Continentes", "No de paises", "Paises por Continentes")
    graficos.bars_graphic_ramp_up(dicionario_teste, "Continentes", "No de paises", "Paises por Continente")

'''mostrar_paises_de_cada_continente()
print("--------------------------")
mostrar_numero_de_paises_de_cada_continente()'''
