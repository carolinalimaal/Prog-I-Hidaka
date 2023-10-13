# Questão 01
def concatenar_strings_v1(lista_1: list, lista_2: list):
    """
    Recebe duas listas de strings de mesmo tamanho e cria outra lista de strings com
    o resultado da concatenação dos elementos correspondentes das listas iniciais.

    Argumentos: 
        lista_strings_1, lista_strings_2.
    Saída: 
        lista_concatenada.
    """
    resultado = []
    for x, y in zip(lista_1, lista_2):
        resultado.append(x + y)
    return resultado


def concatenar_strings_v2(lista_1: list, lista_2: list):
    """
    Recebe duas listas de strings de mesmo tamanho e cria outra lista de strings com
    o resultado da concatenação dos elementos correspondentes das listas iniciais.
    MÉTODO LIST COMPREHENSION.

    Argumentos: 
        lista_strings_1, lista_strings_2.
    Saída: 
        lista_concatenada.
    """
    return [x + y for x, y in zip(lista_1, lista_2)]

# Questão 02
def verificar_numero_primo(numero: int):
    """
    Verifica se o número de entrada é primo ou não.
    
    Argumento: 
        numero_inteiro
    Saída: 
        Valor booleano True (para é primo) ou False (para não é primo)
    """
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True


def encontrar_proximo_primo(numero: int):
    """
    Encontra o próximo primo em relação ao número de entrada. 
    Não leva em consideração o número de entrada, mesmo que ele seja primo.
    
    Argumento: 
        numero_inteiro
    Saída: 
        numero_inteiro_primo
    """
    numero += 1
    while not verificar_numero_primo(numero):
        numero += 1
    return numero


def mapear_lista_numeros_primos(lista_inteiros: list):
    """
    Mapea uma lista de números para uma lista dos menores números 
    primos maiores que os números da lista inicial.
    
    Argumento: 
        lista de inteiros
    Saída: 
        Lista de números inteiros primos.
    """
    return [encontrar_proximo_primo(item) for item in lista_inteiros]

# Questão 03
def filtrar_strings_por_tamanho_v1(lista_strings: list):
    """
    Filtra uma lista de strings para uma outra lista contendo 
    somente strings com tamanho menor que 10.
    
    Argumento: 
        lista_strings
    Saída: 
        lista_strings_filtrada
    """
    lista_filtrada = []
    for item in lista_strings:
        if len(item) < 10:
            lista_filtrada.append(item)
    return sorted(lista_filtrada)


def filtrar_strings_por_tamanho_v2(lista_strings):
    """
    Filtra uma lista de strings para uma outra lista contendo
    somente strings com tamanho menor que 10.
    MÉTODO LIST COMPREHESION
    
    Argumento: 
        Lista de strings
    Saída: 
        Lista de strings filtrada
    """
    return sorted([item
                   for item in lista_strings
                   if len(item) < 10])

# Questão 04
def 

# Questão 05

# Questão 06

# Questão 07

# Questão 08

# Questão 09

# Questão 10

# Questão 11

# Questão 12

# Questão 13

# Questão 14

# Questão 15

# Questão 16

# Questão 17
