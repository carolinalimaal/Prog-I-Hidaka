from random import randint

def verificar_frerquencia_valor(lista_elementos, elemento_desejado):
    """
    Verifica a frenquência de um valor em uma determinada lista 
    Argumentos:
        lista_elementos: Uma lista contendo vários valores iguais e/ou distintos
        elemento_desejado: Valor que se deseja verificar a frenquência
    Saída:
        frequencia: Valor inteiro referente a frenquecia do elemento_desejado
    """
    frequencia = 0
    for item in lista_elementos:
        if item == elemento_desejado:
            frequencia += 1
    return frequencia

def gerar_aleatorio(quantidade, limite):
    return [randint(0, limite) for _ in range(quantidade)]

lista = gerar_aleatorio(1000, 101)
print(f'{lista}\n')
print(verificar_frerquencia_valor(lista, 101))
