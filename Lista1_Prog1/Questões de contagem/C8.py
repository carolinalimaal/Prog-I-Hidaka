def calcular_conceitos_de_notas(lista_conceitos):
    """
    Calcula quantos alunos possuem cada conceito (E, B, R e I).
    Argumento:
        lista_conceitos: Uma lista contendo os conceitos de cada aluno, expresso em string caixa alta
    Saída:
        dicionario_conceitos: Um dicionário contendo a quantidade de alunos que cada conceito possue.
    """
    dicionario_conceitos = {'E': 0,
                            'B': 0,
                            'R': 0,
                            'I': 0}

    for conceito in lista_conceitos:
        for key in dicionario_conceitos:
            if conceito == key:
                dicionario_conceitos[key] += 1
    return dicionario_conceitos


conceitos = ['E', 'E', 'B', 'B', 'R', 'E', 'B', 'R', 'I', 'I', 'R', 'R', 'I']
print(calcular_conceitos_de_notas(conceitos))
