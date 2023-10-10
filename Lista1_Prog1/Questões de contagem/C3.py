def encontrar_aluno_mais_alto(lista_alturas):
    """
    Recebe uma lista contendo valores que representam as alturas, em metro, dos alunos
    da escola. Retorna o maior valor da lista, correspondete a maior altura.
    Argumento:
        lista_alturas: Uma lista contendo valores do tipo float que representam as alturas dos alunos
    Saída:
        max(lista_alturas): O maior valor da lista    
    """
    return f'O aluno mais alto tem {max(lista_alturas)} de altura'

alturas = [1.5, 1.75, 1.67, 1.9, 1.56, 1.89]
print(encontrar_aluno_mais_alto(alturas))
