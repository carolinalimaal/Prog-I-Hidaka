#Questão 01
def concatenar_strings_v1(lista_1, lista_2):
    """
    Recebe duas listas de strings de mesmo tamanho e cria outra lista de strings com o
    resultado da concatenação dos elementos correspondentes das listas iniciais.
    Argumentos: Lista_strings_1, Lista_strings_2.
    Saída: Lista_concatenada.
    """
    resultado = []
    for x, y in zip(lista_1, lista_2):
        resultado.append(x + y)
    return resultado

def concatenar_strings_v2(lista_1, lista_2):
    """
    Recebe duas listas de strings de mesmo tamanho e cria outra lista de strings com o
    resultado da concatenação dos elementos correspondentes das listas iniciais.
    MÉTODO LIST COMPREHENSION.
    Argumentos: Lista_strings_1, Lista_strings_2.
    Saída: Lista_concatenada.
    """
    return [x + y for x, y in zip(lista_1, lista_2)]

#Questão 02
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

#Questão 03
def filtrar_strings_por_tamanho_V1(lista_strings):
    """
    Filtra uma lista de strings para uma outra lista contendo somente strings com tamanho menor que 10.
    Argumento: Lista de strings
    Saída: Lista de strings filtrada
    """
    lista_filtrada = []
    for item in lista_strings:
        if len(item) < 10:
            lista_filtrada.append(item)
    return sorted(lista_filtrada)

def filtrar_strings_por_tamanho_V2(lista_strings):
    """
    Filtra uma lista de strings para uma outra lista contendo somente strings com tamanho menor que 10.
    MÉTODO LIST COMPREHESION
    Argumento: Lista de strings
    Saída: Lista de strings filtrada
    """
    return sorted([item\
                   for item in lista_strings\
                    if len(item) < 10])

#Questão 05

#Questão 06

#Questão 07

#Questão 08

#Questão 09

#Questão 10

#Questão 11

#Questão 12

#Questão 13

#Questão 14

#Questão 15

#Questão 16

#Questão 17

