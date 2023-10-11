import random as r

def busca_binaria(lista_inteiros, numero_buscado):
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
    lista_inteiros = sorted(lista_inteiros)
    inicio = 0
    fim = len(lista_inteiros) - 1
    combinacoes = 0
    while inicio <= fim:
        combinacoes += 1
        meio = (inicio + fim) // 2
        if lista_inteiros[meio] == numero_buscado:
            return True, combinacoes
        elif lista_inteiros[meio] > numero_buscado:
            fim = meio - 1
        else:
            inicio = meio + 1
    return False, combinacoes

def gerar_lista_aleatoria(quantidade, limite):
    return sorted([r.randint(0, limite) for _ in range(quantidade)])

lista = gerar_lista_aleatoria(1000, 500)
print(lista)
print(busca_binaria(lista, 1))
