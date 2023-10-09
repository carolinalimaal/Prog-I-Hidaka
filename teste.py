def teste(lista, valor):
    cont = 0
    lista_ordenada = sorted(lista)
    inicio = 0
    fim = len(lista_ordenada) - 1
    num_meio = lista_ordenada[(inicio + fim) // 2]
    while True:
        if num_meio > valor:
            cont += 1
            inicio = 0
            fim = lista_ordenada.index(num_meio)
            num_meio = lista_ordenada[(inicio + fim) // 2]

        elif num_meio < valor:
            cont += 1
            inicio = lista_ordenada.index(num_meio) + 1
            fim = len(lista_ordenada) - 1
            num_meio = lista_ordenada[(inicio + fim) // 2]

        if num_meio == valor:
            cont += 1
            return True, cont
        else:
            cont += 1
            return False, cont


# 1 5 8 17 33 58 90
listaa = [1, 33, 5, 90, 58, 8, 17]
print(teste(listaa, 90))
print(teste(listaa, 1))
print(teste(listaa, 9))
print(teste(listaa, 8))
