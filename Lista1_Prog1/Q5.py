def filtrar_lista_strings_por_tamanho_v1(lista_string, lista_inteiro):
    """
    Recebe uma lista de strings e uma lista de inteiros. Filtra a lista de strings, em que os elementos da lista filtrada
    devem ter tamanho <= ao número correspodente na lista de inteiros.
    Argumentos: Lista de strings, Lista de inteiros
    Saída: Lista de strings
    """
    lista_filtrada = []
    for x, y in zip(lista_string, lista_inteiro):
        if len(x) <= y:
            lista_filtrada.append(x)
    return lista_filtrada

lista_strings = ['Carolina', 'Pedro', 'eu amo belem']
lista_inteiros = [7, 8, 12]
print(filtrar_lista_strings_por_tamanho_v1(lista_strings, lista_inteiros))

def filtrar_lista_strings_por_tamanho_v2(lista_string, lista_inteiro):
    """
    Recebe uma lista de strings e uma lista de inteiros. Filtra a lista de strings, em que os elementos da lista filtrada.
    MÉTODO LIST COMPREHESION
    devem ter tamanho <= ao número correspodente na lista de inteiros.
    Argumentos: Lista de strings, Lista de inteiros
    Saída: Lista de strings
    """
    return ([x\
            for x, y in zip(lista_string, lista_inteiro)\
            if len(x) <= y])

lista_strings = ['Paula', 'Joao', 'Chocolate ao leite']
lista_inteiros = [4, 8, 20]
print(filtrar_lista_strings_por_tamanho_v2(lista_strings, lista_inteiros))
