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
    return [r.randint(1, limite) for _ in range(quantidade)]

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

# Questão 16 
def verificar_frequencia(lista: list, valor: int):
    freq = 0
    for item in lista:
        if item == valor:
            freq += 1
    return freq

# Questão 17
def verificar_freq(lista: list):
    dic_freq = {1 : 0, 2 : 0,
                3 : 0, 4 : 0,
                5 : 0, 6 : 0,
                7 : 0, 8 : 0,
                9 : 0, 10: 0,
                11: 0, 12: 0,
                13: 0, 14: 0,
                15: 0, 16: 0,
                17: 0, 18: 0,
                19: 0, 20: 0}
    for item in lista:
        dic_freq[item] += 1
    return dic_freq

# Contagem 01
def verificar_tamanho_embalagens(lista_tamanhos: list):
    cont = 0
    for item in lista_tamanhos:
        if item < 7:
            cont += 1
    return cont

# Contagem 02
def verificar_notas_acima_media(lista_notas: list, media: float):
    cont = 0
    for item in lista_notas:
        if item > media:
            cont += 1
    return cont

# Contagem 03
def encontrar_maior_altura(lista_alturas: list):
    return max(lista_alturas)

# Contagem 04
def calcular_media_numeros_pares(lista_numeros: list):
    soma = cont = 0 
    for item in lista_numeros:
        if item % 2 == 0:
            soma += item
            cont += 1
    return soma / cont

# Contagem 05
def verificar_freq_bases_nitrogenadas(lista: list, sequencia: str):
    freq = 0
    for item in lista:
        if item == sequencia:
            freq += 1
    return freq

# Contagem 06
def verificar_itens_inclusos(lista: list, velocidade: int):
    soma = cont = 0
    for item in lista:
        soma += item
        if soma <= velocidade:
            cont += 1
    return cont

# Contagem 07
def sortear_convidados(lista_bilhetes: list):
    cont = 0
    for item in lista_bilhetes:
        if item == (lista_bilhetes.index(item) + 1):
            cont += 1
    return cont

# Contagem 08
def organizar_conceitos(lista_conceitos: list):
    dic_conceitos = {'E': 0,
                     'B': 0,
                     'R': 0,
                     'I': 0}
    for item in lista_conceitos:
        dic_conceitos[item] += 1
    return dic_conceitos

# Contagem 09
def classificar_nivel_seguranca(lista_vulnerabilidades: list):
    dic_classificacao = {'Muito seguro': 0,
                       'Quase seguro': 0,
                       'Inseguro': 0,
                       'Muito inseguro': 0}
    for item in lista_vulnerabilidades:
        if item == 0:
            dic_classificacao['Muito seguro'] += 1
        elif 1 <= item <= 3:
            dic_classificacao['Quase seguro'] += 1
        elif 4 <= item <= 5:
            dic_classificacao['Inseguro'] += 1
        else:
            dic_classificacao['Muito inseguro'] += 1
    return dic_classificacao

# Contagem 10
def filtrar_nomes(lista_nomes: list):
    lista_filtrada = []
    for nome in lista_nomes:
        if nome[0] in 'Rr':
            lista_filtrada.append(nome)
    return lista_filtrada

# Contagem 11
def verificar_validade_produtos(lista_validades: list, mes: int):
    lista_filtrada = []
    for item in lista_validades:
        if item >= mes:
            lista_filtrada.append(item)
    return lista_filtrada

# Contagem 12
def verificar_saldos_positivos(clientes: list, saldos: list):
    lista_filtrada = []
    for nome, saldo in zip(clientes, saldos):
        if saldo > 0:
            lista_filtrada.append(nome)
    return lista_filtrada

# Contagem 13
def verificar_validade_produtos_completo(lista_produtos: list, lista_validades: list, mes: int):
    lista_filtrada = []
    for produto, validade in zip(lista_produtos, lista_validades):
        if validade >= mes:
            lista_filtrada.append([produto, validade])
    return f'Produtos na validade: {lista_filtrada}'

# Contagem 14
def verificar_clientes_na_faixaEtaria(lista_clientes: list, lista_idades: list, faixa_etaria: list):
    lista_filtrada = []
    for cliente, idade in zip(lista_clientes, lista_idades):
        if faixa_etaria[0] <= idade <= faixa_etaria[1]:
            lista_filtrada.append(cliente)
    return lista_filtrada

# Contagem 15
def verificar_numero_par_na_poiscao_par(lista_numeros: list):
    lista_filtrada = []
    for i in range(len(lista_numeros)):
        if i % 2 == 0 and lista_numeros[i] % 2 == 0:
            lista_filtrada.append(lista_numeros[i])
    return f'Quantidade de números: {len(lista_filtrada)} \nNúmeros: {lista_filtrada}'

# Contagem 16
def pesquisar_por_prefixo(lista: list, prefixo: str):
    lista_filtrada = []
    for item in lista:
        if prefixo in item:
            lista_filtrada.append(item)
    return lista_filtrada

# Contagem 17
def verificar_progressao_aritmetica(lista_numeros: list):
    lista_razoes = []
    for i in range(len(lista_numeros) - 1):
        q = lista_numeros[i] - lista_numeros[i+1]
        lista_razoes.append(q)
    if len(set(lista_razoes)) == 1:
        return 'Sim'
    return 'Não'

# Contagem 18
def calcular_distancia_hamming(paciente1: list, paciente2: list):
    cont = 0
    for x, y in zip(paciente1, paciente2):
        if x != y:
            cont += 1
    return cont
