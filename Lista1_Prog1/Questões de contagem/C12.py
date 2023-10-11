def verificar_saldo_positivo(lista_nomes, lista_saldos):
    """
    
    """
    lista_filtrada = []
    for nome, saldo in zip(lista_nomes, lista_saldos):
        if saldo > 0:
            lista_filtrada.append(nome)
    return lista_filtrada

