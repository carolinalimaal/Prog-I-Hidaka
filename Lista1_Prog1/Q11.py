def verificar_numero_primo(numero):
    """
    Verifica se o número de entrada é primo ou não.
    Argumento: Número inteiro.
    Saída: True (para é primo) ou False (para não é primo)
    """
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

def encontrar_maior_primo(lista_inteiros):
    """
    Encontra o maior primo em uma lista de valores inteiros. Caso não tenha números primos na lista,
    a função retorna o valor padrão -1
    Argumento: 
        lista_inteiros: Uma lista contendo números inteiros quaisquer
    Saída:
        max(primos): Maior número primo que está na lista de entrada
    """
    primos = []
    for item in lista_inteiros:
        if verificar_numero_primo(item):
            primos.append(item)
    if len(primos) > 0:
        return max(primos)
    return -1

lista = [2, 6, 8, 10, 12]
print(encontrar_maior_primo(lista))
