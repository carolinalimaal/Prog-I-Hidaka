def calcular_frequencia_bases_nitrogenadas(lista_sequencia_bases, padrao_buscado):
    """
    Calcula a frenquência que uma determinada sequência de bases nitrogenadas 
    aparece numa lista contendo sequências quaisquer de bases nitrogenadas,
    Argumentos: 
        lista_sequencia_bases: Uma lista contendo sequências de bases nitrogendas
        padrao_buscado: O padrão que se busca a frenquência
    Saída: 
        cont: Contador de quantas vezes o padrão apareceu na lista
    """
    cont = 0
    for item in lista_sequencia_bases:
        if item == padrao_buscado:
            cont += 1
    return f'Existem {cont} sequências de bases iguais ao padrão {padrao_buscado}'

lista = ['TACG', 'GAGC', 'ATUC', 'TAGC', 'GAGC', 'AACG', 'TGAC']
padrao = 'GAGC'
print(calcular_frequencia_bases_nitrogenadas(lista, padrao))
