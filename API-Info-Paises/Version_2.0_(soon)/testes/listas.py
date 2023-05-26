lista = [['australia', 'japao', 'russia'], ['inglaterra', 'italia', 'angola']]


def search_indice(lista_de_busca, pais):
    for sub_lista in lista_de_busca:
        if pais in sub_lista:
            return lista_de_busca.index(sub_lista), sub_lista.index(pais)


# teste
print(search_indice(lista, "australia"))  # (0, 0)
print(search_indice(lista, "japao"))  # (0, 1)
print(search_indice(lista, "russia"))  # (0, 2)
print(search_indice(lista, "inglaterra"))  # (1, 0)

print(search_indice(lista, "Brasil"))  # None
