import functions as f

# Questão 1
lista_strings_1 = ['Até ', 'Eu amo ', 'Boa ']
lista_strings_2 = ['logo.', 'Belém', 'jogada!']
print(f.concatenar_strings_v1(lista_strings_1, lista_strings_2))
print(f.concatenar_strings_v2(lista_strings_1, lista_strings_2))

# Questão 2
lista_inteiros = [1, 4, 25, 8, 9, 11, 19, 59, 7]
print(f.mapear_lista_numeros_primos(lista_inteiros))

# Questão 3
lista_strings = ['Gabriel', 'Pedro', 'Carolina', 'Paralelepipedo']
print(f.filtrar_strings_por_tamanho_v1(lista_strings))
print(f.filtrar_strings_por_tamanho_v2(lista_strings))
