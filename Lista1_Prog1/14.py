def buscar_linearmente_numero_inteiro_ordenado(lista_inteiros, numero_buscado):
    """
    Ordena a lista de valores inteiros e busca linearmente um número inteiro específico nessa lista. 
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
    for item in sorted(lista_inteiros):
        if item == numero_buscado:
            contador += 1
            return True, contador
        contador += 1
    return False, contador

lista = [1, 45, 34, 67, 2, 15, 77, 102]
print(buscar_linearmente_numero_inteiro_ordenado(lista, 10))
print(buscar_linearmente_numero_inteiro_ordenado(lista, 1))
print(buscar_linearmente_numero_inteiro_ordenado(lista, 35))
print(buscar_linearmente_numero_inteiro_ordenado(lista, 67))
