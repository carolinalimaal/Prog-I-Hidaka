def verificar_numero_primo(numero):
    """
    Verifica se o número de entrada é primo ou não.
    Argumento: Número inteiro.
    Saída: True (para é primo) ou False (para não é primo)
    """
    for divisor in range(2, divisor):
        if numero % divisor == 0:
            return False
    return True

def encontrar_maior_primo(lista_inteiros):
    """
    
    """
    primos = []
    maior_primo = -1
    for item in lista_inteiros:
        if verificar_numero_primo(item):
            primos.append(item)
    
