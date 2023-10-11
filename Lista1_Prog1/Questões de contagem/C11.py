import random as r

def verificar_validade_produtos(lista_validades, referencia):
    """
    
    """
    lista_produtos_validos = []
    for item in lista_validades:
        if item > referencia:
            lista_produtos_validos.append(item)
    return f'Produtos na validade: {lista_produtos_validos}'

def gerar_lista_aleatoria(quantidade, limite):
    return [r.randint(0, limite) for _ in range(quantidade)]

lista = gerar_lista_aleatoria(20, 12)
print(verificar_validade_produtos(lista, 5))
