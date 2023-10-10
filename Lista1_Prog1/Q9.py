def soma_numeros_reais(lista_float):
    """
    Soma os números reais de uma lista somente quando o item atual é maior que o seguinte.
    Argumentos: 
        lista_float: lista de números reais
    Saída:
        soma: número real
    """
    soma = 0
    for i in range(len(lista_float)-1):
        if lista_float[i] > lista_float[i+1]:
            soma += lista_float[i]
    return soma

lista = [1, 3.29, 2.5, 10, 8.732, 7]
print(soma_numeros_reais(lista))
