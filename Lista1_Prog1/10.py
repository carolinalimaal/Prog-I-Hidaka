def concatenar_lista_strings(lista_strings):
    """
    Recebe uma lista com strings e concatena todos os elementos separados por vírgulas e/ou
    espaços em branco.
    Argumentos: 
        lista_strings: uma lista contendo strings
    Saída: 
        string_concatenada: uma única string com a concatenação das que pertenciam a lista inicial.   
    """
    string_concatenada = ''
    for item in lista_strings:
        aux = ''
        for elemento in list(item):
            if elemento != ' ':
                aux += elemento
        string_concatenada += aux
    return string_concatenada

lista = ['carolina', 'eu amo Belém', 'açaí', 'Always']
print(concatenar_lista_strings(lista))
