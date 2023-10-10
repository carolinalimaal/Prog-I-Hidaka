def verificar_itens_para_sprint_backlog(lista_itens, velocidade):
    """
    Verifica quantos itens da lista de complexidade, respeitando a importância
    de cada um, podem ser inclusos no sprint backlog.
    Para ser incluso, a soma da complexidade do itens deve ser <= a velociade do time.
    Argumento:
        lista_itens: Uma lista contendo valores inteiros que expressam a complexidade de cada item em ordem de importância
    Saída:
        cont: Contador para quantificar quantos itens serão inclusos.
    """
    soma = cont = 0
    for item in lista_itens:
        soma += item
        if soma <= velocidade:
            cont += 1
    return f'{cont} itens podem ser inclusos na sprint backlog'

lista = [2, 3, 4, 7, 1, 2, 30, 13, 25, 1, 3 ]
print(verificar_itens_para_sprint_backlog(lista, 20))
