def calcular_devio_padrao(lista_numeros_reais):
    """
    Calcula o desvio padrão de uma lista de números reais.
    Argumento:
        lista_numeros_reais: Uma lista contendo números reais
    Saída:
        variancia**(1/2) : Valor do desvio padrão 
    """
    soma1 = soma2 = 0
    for item in lista_numeros_reais:
        soma1 += item
    media = soma1/len(lista_numeros_reais)
    for item in lista_numeros_reais:
        soma2 += (item - media)**2
    variancia = soma2/len(lista_numeros_reais)
    return variancia**(1/2)

lista_real = [2, 4, 4, 4, 5, 5, 7, 9]
print(calcular_devio_padrao(lista_real))
