def verificar_alunos_na_media(lista_notas, media):
    """
    Dadas uma lista contendo as notas do alunos e a média escolar, verifica quantos
    alunos estão acima da média estabelecida.
    """
    cont = 0
    for nota in lista_notas:
        if nota > media:
            cont += 1
    return f'Existem {cont} notas acima da média escolar estabelecida,'

notas, media = [8, 8.5, 10, 7.5, 3, 5.5, 4, 3.5], 8
print(verificar_alunos_na_media(notas, media))

notas, media = [3.5, 6, 7.5, 8, 9, 9, 5, 10, 7.5, 8], 7
print(verificar_alunos_na_media(notas, media))
