def reduzir_3listas_em_1lista(lista1, lista2, lista3):
    """
    Recebe 3 listas de inteiros, soma os valores de indices correspodentes e retorna a menor soma.
    Argumentos: 
        lista1: lista de inteiros 
        lista2: lista de inteiros
        lista3: lista de inteiros
    Saída: 
        menor: Número inteiro
    """
    menor = lista1[0] + lista2[0] + lista3[0]
    for item in zip(lista1, lista2, lista3):
        menor = ((menor + sum(item)) - abs(menor-sum(item))) // 2
    return menor

lista_1 = [1,4,17]
lista_2 = [12,5,8]
lista_3 = [3,6,9]

print(reduzir_3listas_em_1lista(lista_1, lista_2, lista_3))
