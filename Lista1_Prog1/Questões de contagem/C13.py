def verificar_validade_produtos(lista_produtos, lista_validades, referencia):
    """
    Verifica a validade de produtos em relação a um mês de referência. Retorna somente os produtos válidos.
    Arguementos:
        lista_produtos: Uma lista contendo os nomes de cada produto
        lista_validades: Uma lista contendo os meses de validade de cada produto
        referencia: Um valor inteiro entre [1,12] que representa o mês
    Saída:
        lista_produtos_filtrados: Uma lista contendo listas que associam o nome do produto com a sua validade
    """
    lista_produtos_filtrados = []
    for produto, validade in zip(lista_produtos, lista_validades):
        if validade > referencia:
            _ = [produto, validade]
            lista_produtos_filtrados.append(_)
    return lista_produtos_filtrados

produtos = ['AA', 'AB', 'BA', 'BB', 'CA', 'AC']
validades = [5, 4, 3, 11, 12, 1]
print(verificar_validade_produtos(produtos, validades, 2))
