from funcoes_indicadores import *
from funcoes_paises import *

# criar objeto Indicador
print(mostrar_id_dos_indicadores())
print(f"\n{'-' * 20}\n")


print(mostrar_indicador_especifico_de_pais_especifico("BR", "77846"))
print(f"\n{'-' * 20}\n")

# criar objeto Pais
print(mostrar_conteudo_de_pais_especifico("BR"))
print(f"\n{'-' * 20}\n")

print(mostrar_todos_os_indicadores_de_um_pais("BR"))
print(f"\n{'-' * 20}\n")

"""
OBS: Todos os indicadores de um pais esta em uma pagina a parte
((endereco a parte))
"""
"""
OBS: O conteudo de cada indicador esta em uma pagina propria
"""

print(mostrar_todos_os_paises_existentes())
print(f"\n{'-' * 20}\n")