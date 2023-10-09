def filtrar_listas_v1(lista_listas):
    """
    Filtra uma lista de listas contendo números inteiros para obter outra lista de listas em que o elemento
    tem a soma maior que o elemente seguinte
    Argumentos: Lista de listas de inteiros
    Saída: Lista 
    """
    lista_filtrada = []
    for i in range(len(lista_listas)-1):
        if sum(lista_listas[i]) > sum(lista_listas[i+1]):
            lista_filtrada.append(lista_listas[i])
    return lista_filtrada

def filtrar_listas_v2(lista_listas):
    """
    Filtra uma lista de listas contendo números inteiros para obter outra lista de listas em que o elemento
    MÉTODO LIST COMPREHESION
    tem a soma maior que o elemente seguinte
    Argumentos: Lista de listas de inteiros
    Saída: Lista 
    """
    return [lista_listas[i]\
            for i in range(len(lista_listas) - 1)\
            if sum(lista_listas[i]) > sum(lista_listas[i+1])]

lista_de_listas = [[4, 5, 6], [1, 2, 3], [7, 8, 9], [3, 2, 0]]
print(filtrar_listas_v1(lista_de_listas))
print(filtrar_listas_v2(lista_de_listas))
