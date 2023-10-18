def mapear_inteiros(number):
    if type(number) is int:
        return number


numberList = [1.3456, 8, 9.323, 0, '222']

lista = list(map(mapear_inteiros, numberList))
print(lista)

lista = list(map(int, numberList))
print(lista)

def mapear_menor_valor(v1, v2, v3):
    return min(v1,v2,v3)

l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 8, 10]
l3 = [1, 3, 5, 7, 9]

menor_valor = list(map(lambda v1, v2, v3: min(v1,v2,v3), l1, l2, l3))
print(menor_valor)
