import functions as f

# Questão 01
lista_strings1 = ['a', 'b', 'c', 'd']
lista_strings2 = ['w', 'x', 'y', 'z']
print(f.concatenar_elementos(lista_strings1, lista_strings2))
print(f.concatenar_elementos_v2(lista_strings1, lista_strings2))

# Questão 02
numeros_inteiros = [2, 6, 4, 9, 15, 27]
print(f.mapear_primos(numeros_inteiros))

# Questão 03
strings = ['Carolina', 'Paralelepipedo', 'Maria', 'Até logo!']
print(f.filtrar_strings_por_tamanho(strings))
print(f.filtrar_strings_por_tamanho_v2(strings))

# Questão 04
lista_heterogenea = [[1, 4.5, 'bom dia', 8], [9.0, 'carol', 19, 2.78]]
print(f.filtrar_listas_hetereogenas(lista_heterogenea))
print(f.filtrar_listas_hetereogenas_v2(lista_heterogenea))

# Questão 05
strings = ['Carolina', 'Gabriel', 'Sony', 'Nintendo']
inteiros = [7, 9, 3, 10]
print(f.filtrar_strings(strings, inteiros))
print(f.filtrar_strings_v2(strings, inteiros))

# Questão 06
lista_sublistas = [[5, 2, 7], [5, 8, 0], [11, 1, 3], []]
print(f.filtrar_sublistas(lista_sublistas))
print(f.filtrar_sublistas_v2(lista_sublistas))

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

# Questão 16
lista = f.gerar_aleatorio(1000, 100)
print(f.verificar_frequencia(lista, 1))

# Questão 17
lista = f.gerar_aleatorio(1000, 20)
print(f.verificar_freq(lista))

# Contagem 01
tamanhos_embalagens = [8,18,4,20,1,12]
print(f.verificar_tamanho_embalagens(tamanhos_embalagens))

# Contagem 02
notas = [3.5, 6, 7.5, 8, 9, 9, 5, 10, 7.5, 8]
print(f.verificar_notas_acima_media(notas, 7))

# Contagem 03
alturas = [1.5, 1.75, 1.67, 1.9, 1.56, 1.89 ]
print(f.encontrar_maior_altura(alturas))

# Contagem 04
numeros = [3, 5, 4, 6, 3, 2, 8, 10]
print(f.calcular_media_numeros_pares(numeros))

# Contagem 05
sequencia_bases = ['TACG', 'GAGC', 'ATUC', 'TAGC', 'GAGC']
print(f.verificar_freq_bases_nitrogenadas(sequencia_bases, 'GAGC'))

# Contagem 06
lista_complexidade = [5, 3, 4, 7, 10, 2, 1, 13, 25, 1, 1, 8]
print(f.verificar_itens_inclusos(lista_complexidade, 32))

# Contagem 07
bilhetes = [3, 2, 5, 4, 8, 6, 7, 10, 12, 13, 11]
print(f.sortear_convidados(bilhetes))

# Contagem 08
conceitos = ['E','E','B','B','R','E','B','R','I','I','R','R','I']
print(f.organizar_conceitos(conceitos))

# Contagem 09
vulnerabilidades = [1, 5, 6, 7, 3, 2, 2, 1, 0, 0, 0, 0]
print(f.classificar_nivel_seguranca(vulnerabilidades))

# Contagem 10
nomes = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
print(f.filtrar_nomes(nomes))
print(f.filtrar_nomes_v2(nomes))

# Contagem 11
validades = [2, 3, 4, 7, 1, 2, 1, 3]
print(f.verificar_validade_produtos(validades, 3))
print(f.verificar_validade_produtos_v2(validades, 3))

# Contagem 12
cliente = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
dinheiro = [100, -500, -1, 1500, 90]
print(f.verificar_saldos_positivos(cliente, dinheiro))
print(f.verificar_saldos_positivos_v2(cliente, dinheiro))

# Contagem 13
validades = [5, 4, 3, 11, 12, 1]
produtos = ['AA','AB','BA','BB','CA','AC']
print(f.verificar_validade_produtos_completo(produtos, validades, 8))
print(f.verificar_validade_produtos_completo_v2(produtos, validades, 8))

# Contagem 14
clientes = ['Ramon', 'Arnaldo', 'Raquel', 'Pedro', 'Rafael']
idades = [23, 45, 27, 60, 45]
print(f.verificar_clientes_na_faixaEtaria(clientes, idades, [20,30]))
print(f.verificar_clientes_na_faixaEtaria_v2(clientes, idades, [20,30]))

# Contagem 15
numeros = [1, 3, 4, 5, 6, 7, 8, 9]
print(f.verificar_numero_par_na_poiscao_par(numeros))
print(f.verificar_numero_par_na_poiscao_par_v2(numeros))

# Contagem 16
nomes = ['Amanda', 'Amaral', 'Arnaldo', 'Bruno']
print(f.pesquisar_por_prefixo(nomes, 'Ama'))
print(f.pesquisar_por_prefixo_v2(nomes, 'Ama'))

# Contagem 17
sequencia = [1, 3, 4, 5, 6, 7, 8, 9]
print(f.verificar_progressao_aritmetica(sequencia))

# Contagem 18
p1 = [1, 0, 0, 1, 1, 0, 1, 0]
p2 = [1, 1, 1, 1, 1, 1, 1, 1]
print(f.calcular_distancia_hamming(p1, p2))
