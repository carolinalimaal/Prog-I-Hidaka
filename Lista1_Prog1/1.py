def concatenar_strings_v1(lista_1, lista_2):
    """
    Recebe duas listas de strings de mesmo tamanho e cria outra lista de strings com o
    resultado da concatenação dos elementos correspondentes das listas iniciais.
    Argumentos: Lista_strings_1, Lista_strings_2.
    Saída: Lista_concatenada.
    """
    resultado = []
    for x, y in zip(lista_1, lista_2):
        resultado.append(x + y)
    return resultado

def concatenar_strings_v2(lista_1, lista_2):
    """
    Recebe duas listas de strings de mesmo tamanho e cria outra lista de strings com o
    resultado da concatenação dos elementos correspondentes das listas iniciais.
    MÉTODO LIST COMPREHENSION.
    Argumentos: Lista_strings_1, Lista_strings_2.
    Saída: Lista_concatenada.
    """
    return [x + y for x, y in zip(lista_1, lista_2)]

lista1 = ['a', 'b', 'c', 't']
lista2 = ['h', 'j', 'k', 'p']
print(concatenar_strings_v1(lista1, lista2))

print(concatenar_strings_v2(lista2, lista1))
