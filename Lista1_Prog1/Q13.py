def buscar_numero_inteiro_na_lista(lista_numeros_inteiros, numero_buscado):
    """
    Busca linearmente um número inteiro específico numa lista contendo números inteiros. 
    Se achar o valor, a função retorna True e o número de comparações feitas até encontrar o valor. 
    Caso, contrário, retorna False e o número de comparações feitas até encontrar o valor.
    Argumentos:
        lista_numeros_inteiros: Uma lista contendo valores inteiros
        numero_buscado: Valor inteiro que se deseja encontrar na lista
    Saída:
        True (para quando encontrar o valor) ou False (para quando não encontrar o valor)
        contador: Número de comparações até finalizar a busca
    """
    contador = 0
    for item in lista_numeros_inteiros:
        if item == numero_buscado:
            contador += 1
            return True, contador
        contador += 1
    return False, contador

from random import randint

def gerar_aleatorio(quantidade, limite):
    return [randint(0, limite) for _ in range(quantidade)]

soma = 0
for _ in range(1000):
    lista = gerar_aleatorio(1000, 500)
    lista.sort()
    _, cont = buscar_numero_inteiro_na_lista(lista, randint(1, 500))
    soma += cont
print(soma/1000)
