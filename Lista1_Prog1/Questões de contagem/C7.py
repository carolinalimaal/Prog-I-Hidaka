def calcular_numero_premiados(lista_bilhetes):
    """
    Calcula quantos convidados serão premiados, seguindo o padrão de receber um bilhete e registrar a ordem de chegada.
    Será premiados que tiver o número do bilhete igual a sua ordem de chegada.
    Argumento:
        lista_bilhetes: Uma lista contendo os números dos bilhetes
    Saída:
        cont: Quantidade de convidados que foram premiados.
    """
    bilhetes_sorteados = 0
    for item in lista_bilhetes:
        ordem_chegada = lista_bilhetes.index(item) + 1
        if item == ordem_chegada:
            bilhetes_sorteados += 1
    return f'{bilhetes_sorteados} convidados serão premiados.'


bilhetes = [5, 3, 7, 13, 11, 9, 5, 8, 1, 10 ]
print(calcular_numero_premiados(bilhetes))
