# Exemplos de manipulação de listas, slice...

def criar_lista_reversa(lista):
    return lista[::-1]


def criar_sublista_index_impar(lista):
    return lista[1::2]


def criar_sublista_primeira_metade(lista):
    fim = len(lista)//2
    return lista[:fim]


def criar_sublista_segunda_metade(lista):
    inicio = len(lista)//2
    return lista[inicio:]


# Exemplos de redução

def somar_lista(lista):
    total = 0
    for valor in lista:
        total += valor
    return total


def encontrar_maior_valor_lista(lista):
    maior = lista[0]
    for valor in lista:
        maior = ((maior + valor) + abs(maior - valor)) // 2
    return maior


def calcular_saldo_medio(cadastro):
    saldo_medio = 0
    for elemento in cadastro:
        saldo_medio += elemento['saldo']
    return saldo_medio/len(cadastro)

# Exemplos de filtros


def filtrar_email(cadastro, provedor_email):
    lista_filtrada = []
    for elemento in cadastro:
        if provedor_email in elemento['e-mail']:
            lista_filtrada.append(elemento['e-mail'])
    return lista_filtrada


def filtrar_por_tipo(lista, tipo):
    lista_filtrada = []
    for item in lista:
        if type(item) == tipo:
            lista_filtrada.append(item)
    return lista_filtrada

# Exemplos de mapeamento


def extrair_nomes(cadastro):
    lista_nomes = []
    for elemento in cadastro:
        lista_nomes.append(elemento['nome'])
    return lista_nomes


def formatar_caixa_alta(lista_nomes):
    lista_formatada = []
    for nome in lista_nomes:
        lista_formatada.append(nome.upper())
    return lista_formatada


def formatar_caixa_baixa(lista_nomes):
    lista_formatada = []
    for nome in lista_nomes:
        lista_formatada.append(nome.lower())
    return lista_formatada


def formatar_nomes(lista_nomes, tipo_formato):
    if tipo_formato == 'CAIXA_ALTA':
        return formatar_caixa_alta(lista_nomes)
    elif tipo_formato == 'CAIXA_BAIXA':
        return formatar_caixa_baixa(lista_nomes)
    else:
        return 'Formato inválido, o segundo argumento não é válido.'


def calcular_tamanho_nomes(lista):
    return [len(item) for item in lista]


def criar_lista_cadastros(nomes, emails):
    cadastro = []
    for nome, email in zip(nomes, emails):
        cadastro.append({
            'nome': nome,
            'e-mail': email
        })
    return cadastro


# Dada uma lista de números reais, faça um mapeamento para obter uma lista de números inteiros tal que:
# 1) Se o valor decimal for par, obtenha o número inteiro que seja o maior inteiro menor que o real analisado
# 2) Se o valor decima for impar, obtenha o número inteiro que seja o menor inteiro maior que o real analisado

def separar_parte_decimal(numero):
    x1 = str(numero)
    idx = x1.index('.')
    x2 = x1[idx+1:]
    return int(x2)


def mapear_inteiro(numero):
    import math as m
    num = separar_parte_decimal(numero)
    if num % 2 == 0:
        return m.floor(numero)
    else:
        return m.ceil(numero)


def transformar_real_para_inteiro(lista_numeros):
    return [mapear_inteiro(item) for item in lista_numeros]


# Dada 3 listas de números reais faça o mapeamento para obter uma lista onde cada elemento seja igual a
# soma do maior e do menor elementos de idx correspondentes
def mapear_soma_do_maior_e_menor(lista1, lista2, lista3):
    return [
        max(item) + min(item)
        for item in zip(lista1, lista2, lista3)
    ]


# Dada uma lista de números inteiros, construa a lista reversa e faça o filtro para obter somente os
# elementos que são iguais aos da lista original
def criar_lista_numeros_iguais_correspondentes(lista_numeros):
    return [
        num1
        for num1, num2 in zip(lista_numeros, lista_numeros[::-1])
        if num1 == num2
    ]


# Dada uma lista de strings, faça uma redução para determinar o tamanho da maior string, retorne:
# o valor encontrado, a string em si e o index da lista que a string está
def achar_maior_string(lista):
    dados_maior_string = {
        'valor': lista[0],
        'indice': 0,
        'tamanho': len(lista[0])
    }
    for item in lista[1:]:
        if len(item) > (dados_maior_string['tamanho']):
            dados_maior_string['valor'] = item
            dados_maior_string['indice'] = lista.index(item)
            dados_maior_string['tamanho'] = len(item)
    return dados_maior_string
