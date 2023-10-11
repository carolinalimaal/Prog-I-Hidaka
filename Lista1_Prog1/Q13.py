from random import randint


def busca_linear(lista_numeros_inteiros, numero_buscado):
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

#Para gerar uma lista aleatória
def gerar_lista_aleatoria(quantidade, limite):
    return [randint(0, limite) for _ in range(quantidade)]


# Para calcular quantas comparações foram feitas para achar um determinado valor gerado aleatoriamente
soma = 0
for _ in range(1000):
    lista = gerar_lista_aleatoria(1000, 500)
    lista.sort()
    _, cont = busca_linear(lista, randint(1, 500))
    soma += cont
print(soma/1000)
