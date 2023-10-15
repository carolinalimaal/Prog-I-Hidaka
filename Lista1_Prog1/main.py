import functions as f

# Questão 01
lista_strings1 = ['a', 'b', 'c', 'd']
lista_strings2 = ['w', 'x', 'y', 'z']
print(f.concatenar_elementos(lista_strings1, lista_strings2))

# Questão 02
numeros_inteiros = [2, 6, 4, 9, 15, 27]
print(f.mapear_primos(numeros_inteiros))

# Questão 03
strings = ['Carolina', 'Paralelepipedo', 'Maria', 'Até logo!']
print(f.filtrar_strings_por_tamanho(strings))

# Questão 04
lista_heterogenea = [[1, 4.5, 'bom dia', 8], [9.0, 'carol', 19, 2.78]]
print(f.filtrar_listas_hetereogenas(lista_heterogenea))

# Questão 05
strings = ['Carolina', 'Gabriel', 'Sony', 'Nintendo']
inteiros = [7, 9, 3, 10]
print(f.filtrar_strings(strings, inteiros))

# Questão 06
lista_sublistas = [[5, 2, 7], [5, 8, 0], [11, 1, 3], []]
print(f.filtrar_sublistas(lista_sublistas))

#Questão 07
l1 = [3, 1, 8]
l2 = [4, 6, 5]
l3 = [9, 4, 1]
print(f.encontrar_menor_soma(l1, l2, l3))

# Questão 08
strings = ['Gabe', 'Infernape', 'Lucario', 'Garchomp']
print(f.encontrar_maior_string(strings))

# Questão 09
num_reais = [2.0, 1.978, 0.89764, 5.072395, 5.000017]
print(f.somar_valores_reais(num_reais))

# Questão 10
strings = ['Eu', 'amo ', 'o frio!', ' -As pessoas', 'são mais elegantes.']
print(f.concatenar_strings_separadas_por_vírgula_espaco(strings))

# Questão 11
inteiros = [3, 5, 9, 11, 2, 13, 17]
print(f.encontrar_maior_primo(inteiros))

# Questão 12
numeros = [1.55, 1.7, 1.8]
print(f.calcular_desvio_padrão(numeros))

# Questão 13
lista_numeros = f.gerar_aleatorio(100, 50)
print(lista_numeros)
print(f.busca_linear(lista_numeros, 1))

# Questão 14
print(sorted(lista_numeros))
print(f.busca_linear_ordenada(lista_numeros, 1))

# Questão 15
lista_numeros = f.gerar_aleatorio(10, 5)
print(sorted(lista_numeros))
print(f.busca_binaria(sorted(lista_numeros), 1))
