def classificar_classes_vulnerabilidade(lista_vulnerabilidade):
    """
    Classifica a classe de vulnerabilidade dos softwares.
    Argumento:
        lista_vulnerabilidades: Uma lista contendo a quantidade de vulnerabilidades que cada software possui
    Saída:
        dicionario_classes_vulnerabilidade: Um dicionário que contém o número de softwares que cada classe de vulnerabilidade possui
    """
    dicionario_classes_vulnerabilidade = {'Muito seguro' : 0,
                                          'Quase seguro' : 0,
                                          'Inseguro' : 0,
                                          'Muito inseguro' : 0}
    for item in lista_vulnerabilidade:
        if item == 0:
            dicionario_classes_vulnerabilidade['Muito seguro'] += 1
        elif 1 <= item <= 3:
            dicionario_classes_vulnerabilidade['Quase seguro'] += 1
        elif 4 <= item <= 5:
            dicionario_classes_vulnerabilidade['Inseguro'] += 1
        else:
            dicionario_classes_vulnerabilidade['Muito inseguro'] += 1

    return dicionario_classes_vulnerabilidade

lista = [0, 0 ,1, 3, 2, 4, 5, 6, 1, 2, 7]
print(classificar_classes_vulnerabilidade(lista))