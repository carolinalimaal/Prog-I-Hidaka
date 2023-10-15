# Questão 01
def concatenar_elementos(lista1: list, lista2: list):
    lista_concatenada = []
    for x, y in zip(lista1, lista2):
        lista_concatenada.append(x + y)
    return lista_concatenada

# Questão 02
def encontrar_primo(numero: int):
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

def encontrar_proximo_primo(numero:int):
    numero += 1
    while not encontrar_primo(numero):
        numero += 1
    return numero

def mapear_primos(lista_inteiros: list):
    return [encontrar_proximo_primo(item) for item in lista_inteiros]

# Questão 03
def filtrar_strings_por_tamanho(lista_strings: list):
    lista_filtrada = []
    for item in lista_strings:
        if len(item) < 10:
            lista_filtrada.append(item)
    return lista_filtrada

# Questão 04
def filtrar_por_tipo(lista: list, tipo: type):
    lista_filtrada = []
    for item in lista:
        if type(item) == tipo:
            lista_filtrada.append(item)
    return lista_filtrada

def filtrar_listas_hetereogenas(lista: list):
    lista_map = []
    for sublista in lista:
        lista_map.append(filtrar_por_tipo(sublista, int))
    return lista_map

# Questão 05
def filtrar_strings(lista_strings: list, lista_inteiros: list):
    lista_filtrada = []
    for string, inteiro in zip(lista_strings, lista_inteiros):
        if len(string) <= inteiro:
            lista_filtrada.append(string)
    return lista_filtrada

# Questão 06
def filtrar_sublistas(lista: list):
    lista_filtrada = []
    for idx in range(0, len(lista) - 1):
        if sum(lista[idx]) > sum(lista[idx + 1]):
            lista_filtrada.append(lista[idx])
    return lista_filtrada

# Questão 07
def encontrar_menor_soma(lista1: list, lista2: list, lista3: list):
    menor = lista1[0] + lista2[0] + lista3[0]
    for x, y, z in zip(lista1, lista2, lista3):
        menor = (((x + y + z) + menor) - abs((x + y + z) - menor) ) // 2
    return menor

# Questão 08
def encontrar_maior_string(lista_strings: list):
    tamanho = len(lista_strings[0])
    idx = 0
    for item in lista_strings:
        if len(item) > tamanho:
            tamanho = len(item)
            idx = lista_strings.index(item)
    return f'A maior string é {lista_strings[idx]}, com {tamanho} de tamanho e está no indice {idx}'

# Questão 09
def somar_valores_reais(lista: list):
    soma = 0
    for idx in range(0, len(lista) - 1):
        if lista[idx] > lista[idx + 1]:
            soma += lista[idx]
    return soma

# Questão 10
def concatenar_strings_separadas_por_vírgula_espaco(lista: list):
    string_concatenada = ''
    for string in lista:
        for elemento in string:
            if elemento != ' ':
                string_concatenada += elemento
    return string_concatenada

# Questão 11
def encontrar_maior_primo(lista: list):
    maior = -1
    idx_maior = -1
    for item in lista:
        if encontrar_primo(item):
            maior = (maior + item + abs(maior - item)) // 2
            idx_maior = lista.index(maior)
    return maior, idx_maior

# Questão 12
def calcular_desvio_padrão(lista: list):
    soma = 0
    for item in lista:
        soma += item
    media = soma / len(lista)
    variancia = 0
    for item in lista:
        variancia += (item - media)**2
    desvio_padrao = (variancia / len(lista))**(1/2)
    return desvio_padrao

# Questão 13
import random as r
def gerar_aleatorio(quantidade: int, limite: int):
    return [r.randint(0, limite) for _ in range(quantidade)]

def busca_linear(lista: list, valor: int):
    comparacoes = 0
    for item in lista:
        comparacoes += 1
        if item == valor:
            return True, comparacoes
    return False, comparacoes

# Questão 14
def busca_linear_ordenada(lista: list, valor: int):
    lista = sorted(lista)
    comparacoes = 0
    for item in lista:
        comparacoes += 1
        if item == valor:
            return True, comparacoes
    return False, comparacoes

# Questão 15
def busca_binaria(lista: list, valor:int):
    comparacoes = 0 
    I = 0 
    F = len(lista) - 1
    M = (I + F) // 2
    while I <= F:
        if lista[M] == valor:
            comparacoes += 1
            return True, comparacoes
        elif lista[M] > valor:
            comparacoes += 1
            F = M - 1
            M = (I + F) // 2
        else:
            comparacoes += 1
            I = M + 1
            M = (I + F) // 2
    return False, comparacoes
