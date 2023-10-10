def busca_binaria(lista, numero_buscado):
    """
    Ordena a lista de valores inteiros e faz a busca binária de um número inteiro específico nessa lista. 
    Se achar o valor, a função retorna True e o número de comparações feitas até encontrar o valor. 
    Caso, contrário, retorna False e o número de comparações feitas até encontrar o valor.
    Argumentos:
        lista_inteiros: Uma lista contendo valores inteiros
        numero_buscado: Valor inteiro que se deseja encontrar na lista
    Saída:
        True (para quando encontrar o valor) ou False (para quando não encontrar o valor)
        contador: Número de comparações até finalizar a busca
    """
    lista = sorted(lista)
    inicio = 0
    fim = len(lista) - 1
    combinacoes = 0
    while inicio <= fim:
        combinacoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == numero_buscado:
            return True, combinacoes
        elif lista[meio] > numero_buscado:
            fim = meio - 1
        else:
            inicio = meio + 1
    return False, combinacoes

lista = [1, 33, 5, 90, 58, 8, 17]
print(busca_binaria(lista, 90))
print(busca_binaria(lista, 1))
print(busca_binaria(lista, 9))
print(busca_binaria(lista, 8))
