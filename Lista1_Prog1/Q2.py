def verificar_numero_primo(numero):
    """
    Verifica se o número de entrada é primo ou não.
    Argumento: Número inteiro.
    Saída: Valor booleano True (para é primo) ou False (para não é primo)
    """
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

def encontrar_proximo_primo(numero):
    """
    Encontra o próximo primo em relação ao número de entrada. Não leva em consideração o número de entrada, mesmo que ele seja primo.
    Argumento: Número inteiro.
    Saída: Número inteiro primo.
    """
    numero +=1
    while not verificar_numero_primo(numero):
        numero += 1
    return numero

def mapear_lista_numeros_primos(lista):
    """
    Mapea uma lista de números para uma lista dos menores números primos maiores que os números da lista inicial.
    Argumento: Lista de inteiros
    Saída: Lista de números inteiros primos.
    """
    return [encontrar_proximo_primo(item) for item in lista]


lista_numeros = [45, 53, 16, 9, 11, 5, 3, 10, 13, 27]
print(mapear_lista_numeros_primos(lista_numeros))
