def encontrar_maior_string(lista_strings):
    """
    Encontrar o tamanho da maior string e o indice correspodente. Se mais de uma tiver o mesmo tamanho, irá retornar a primeira.
    Argumento: 
        lista_strings: list
    Saída: 
        tamanho: inteiro
        idx: inteiro
    """
    tamanho = len(lista_strings[0])
    idx = 0
    for item in lista_strings:
        if len(item) > tamanho:
            tamanho = len(item)
            idx = lista_strings.index(item)
    return tamanho, idx

lista = ['Carolina', 'Paula', 'Joao', 'Paralelepipedo']
tamanho_maior, idx_maior = encontrar_maior_string(lista)
print(f'A maior string tem tamanho {tamanho_maior} e está no indice {idx_maior}')
