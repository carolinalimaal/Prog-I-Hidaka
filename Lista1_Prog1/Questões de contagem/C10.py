def filtrar_nomes_pela_inicial_R(lista_nomes):
    """
    Filtra os nomes de uma lista pela letra R
    Argumento:
        lista_nomes: Uma lista contendo nomes (tipo string)
    Saída:
        lista_filtrada: Uma lista contendo somente os nomes que iniciam com R
    """
    lista_filtrada = []
    for nome in lista_nomes:
        if list(nome)[0] == 'R':
            lista_filtrada.append(nome)
    return lista_filtrada

nomes = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
print(filtrar_nomes_pela_inicial_R(nomes))
