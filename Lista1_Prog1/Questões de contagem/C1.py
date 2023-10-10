def verificar_tamanho_embalagem_caramelo(lista_tamanhos):
    """
    Verifica se o tamanho das embalagens, elementos da lista,
    está fora do padrão estabelecido, menor que 7.
    Argumento:
        lista_tamanhos: Uma lista contendo valores inteiros que reprensentam os tamanhos das embalagens
    Saída:
        cont: Valor inteiro que contabiliza quantas embalagens estão fora do padrão
    """
    tamanho_minimo = 7
    cont = 0
    for item in lista_tamanhos:
        if item < tamanho_minimo:
            cont += 1
    return f'Existem {cont} embalagens fora do padrão estabelecido'

lista1 = [7,6,5,4,3,6,7,8,20,3,12 ]
lista2 = [3,5,8,2,11,1,4,4,4,4]

print(verificar_tamanho_embalagem_caramelo(lista1))
print(verificar_tamanho_embalagem_caramelo(lista2))
