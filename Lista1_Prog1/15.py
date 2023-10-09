def busca_binaria_inteiros(lista_inteiros, numero_buscado):
    """
    Ordena a lista de valores inteiros e faz a busca binária um número inteiro específico nessa lista. 
    Se achar o valor, a função retorna True e o número de comparações feitas até encontrar o valor. 
    Caso, contrário, retorna False e o número de comparações feitas até encontrar o valor.
    Argumentos:
        lista_inteiros: Uma lista contendo valores inteiros
        numero_buscado: Valor inteiro que se deseja encontrar na lista
    Saída:
        True (para quando encontrar o valor) ou False (para quando não encontrar o valor)
        contador: Número de comparações até finalizar a busca
    """
    lista_ordenada = sorted(lista_inteiros)
    fim = len(lista_inteiros)-1
    numero_do_meio = lista_ordenada[fim // 2]
    contador = 0
    while True:
        if (len(lista_ordenada) == 1 and numero_do_meio != numero_buscado) or (numero_buscado not in lista_inteiros):
            contador += 1
            return False, contador

        if numero_do_meio > numero_buscado:
            contador += 1
            fim = lista_ordenada.index(numero_do_meio)
            numero_do_meio = lista_ordenada[fim // 2]

        elif numero_do_meio < numero_buscado:
            contador += 1
            inicio = lista_ordenada.index(numero_do_meio) + 1
            fim = len(lista_ordenada) - 1
            numero_do_meio = lista_ordenada[(inicio + fim) // 2]
        else:
            contador += 1
            return True, contador

# 1 5 9 17 33 58 90
lista = [1, 33, 5, 90, 58, 8, 17]
print(busca_binaria_inteiros(lista, 90))
print(busca_binaria_inteiros(lista, 1))
print(busca_binaria_inteiros(lista, 9))
print(busca_binaria_inteiros(lista, 8))
