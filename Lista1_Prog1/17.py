from random import randint


def verificar_frerquencia_valor(lista_elementos):
    """
    Verifica a frenquência de um valor em uma determinada lista 
    Argumentos:
        lista_elementos: Uma lista contendo vários valores iguais e/ou distintos
    Saída:
        frequencia: Dicionário referente às frenquecias dos elementos da lista
    """
    dicionario_frequencia = {1: 0,
                             2: 0,
                             3: 0,
                             4: 0,
                             5: 0,
                             6: 0,
                             7: 0,
                             8: 0,
                             9: 0,
                             10: 0,
                             11: 0,
                             12: 0,
                             13: 0,
                             14: 0,
                             15: 0,
                             16: 0,
                             17: 0,
                             18: 0,
                             19: 0,
                             20: 0}
    for item in lista_elementos:
        for key in range(1, 21):
            if item == key:
                dicionario_frequencia[key] += 1
    return dicionario_frequencia


lista = []
for i in range(1000):
    lista.append(randint(1, 21))
print(f'{lista}\n')

print(verificar_frerquencia_valor(lista))
