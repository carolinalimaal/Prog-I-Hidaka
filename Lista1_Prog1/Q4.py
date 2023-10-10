def filtrar_por_tipo(lista, tipo):
    """
    Filtra uma lista para uma outra lista contendo somente os elementos do tipo especificado.
    Argumento: Lista, tipo de dado
    Saída: Lista filtrada
    """
    lista_filtrada = []
    for item in lista:
        if type(item) == tipo:
            lista_filtrada.append(item)
    return lista_filtrada

def filtrar_listas_homogeneas_v1(lista_heterogenea):
    """
    Filtra uma lista de listas heterogênea para uma outra lista contendo somente as listas com os elementos do tipo inteiro.
    Argumento: Lista de listas, Tipo inteiro
    Saída: Lista de listas somente com elementos do tipo inteiro
    """
    lista_map = []
    for item in lista_heterogenea:
        lista_map.append(filtrar_por_tipo(item, int))
    return lista_map

def filtrar_listas_homogeneas_v2(lista_heterogenea):
    """
    Filtra uma lista de listas heterogênea para uma outra lista contendo somente as listas com os elementos do tipo inteiro.
    MÉTODO LIST COMPREHESION.
    Argumento: Lista de listas, Tipo inteiro
    Saída: Lista de listas somente com elementos do tipo inteiro
    """
    return [filtrar_por_tipo(item, int)\
            for item in lista_heterogenea]

lista_het = [[1, 2, 3.3, 4], ['A', 2, 'B'], ['D', 2.5]]
print(filtrar_listas_homogeneas_v1(lista_het))
print(filtrar_listas_homogeneas_v2(lista_het))
