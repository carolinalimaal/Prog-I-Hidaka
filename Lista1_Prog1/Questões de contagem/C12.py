def verificar_saldo_positivo(lista_nomes, lista_saldos):
    """
    Verifica se o saldo que corresponde e pessoa do mesmo indice é positivo. Se sim, filtra a lista de nomes.
    Argumentos: 
        lista_nomes: Uma lista contendo o nome das pessoas
        lista_saldos: Uma lista contendo o saldo bancário das pessoas
    Saída:
        lista_filtrada: Uma lista somente com os valores filtrados
    """
    lista_filtrada = []
    for nome, saldo in zip(lista_nomes, lista_saldos):
        if saldo > 0:
            lista_filtrada.append(nome)
    return lista_filtrada

nomes = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
saldos = [100, -500, -1, 1500, 90]

print(verificar_saldo_positivo(nomes, saldos))
