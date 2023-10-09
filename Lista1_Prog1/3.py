def filtrar_strings_por_tamanho_V1(lista_strings):
    """
    Filtra uma lista de strings para uma outra lista contendo somente strings com tamanho menor que 10.
    Argumento: Lista de strings
    Saída: Lista de strings filtrada
    """
    lista_filtrada = []
    for item in lista_strings:
        if len(item) < 10:
            lista_filtrada.append(item)
    return sorted(lista_filtrada)

def filtrar_strings_por_tamanho_V2(lista_strings):
    """
    Filtra uma lista de strings para uma outra lista contendo somente strings com tamanho menor que 10.
    MÉTODO LIST COMPREHESION
    Argumento: Lista de strings
    Saída: Lista de strings filtrada
    """
    return sorted([item\
                   for item in lista_strings\
                    if len(item) < 10])

print(filtrar_strings_por_tamanho_V1(['carolina', 'paula', 'marcelo']))
print(filtrar_strings_por_tamanho_V2(['carolina', 'paula', 'pedro', 'eu amo belém']))
