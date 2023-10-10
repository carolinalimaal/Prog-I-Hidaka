def calcular_media_numeros_pares(lista_inteiros):
    """
    Calcula a média aritimética entre os números pares contidos na lista.
    Argumento:
        lista_inteiros: Uma lista contendo valores inteiros
    Saída:
        media: Média aritimética entre os números pares da lista de entrada
    """
    soma = cont = 0
    for numero in lista_inteiros:
        if numero % 2 == 0:
            soma += numero
            cont += 1
    return f'A média entre os números pares é {soma / cont}'

lista = [5, 4, 8, 9, 10, 12, 4, 3, 7, 4]
print(calcular_media_numeros_pares(lista))
