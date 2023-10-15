import funcoes as f

lista = [1,2,3,4,5]

print(f.criar_lista_reversa(lista))

print(f.criar_sublista_index_impar(lista))

print(f.criar_sublista_primeira_metade(lista))

print(f.criar_sublista_segunda_metade(lista))

print(f.somar_lista(lista))

print(f.encontrar_maior_valor_lista(lista))

cadastro = [
    {
    'nome': 'renato',
    'e-mail': 'renato@email.com',
    'saldo': 1024
    },
    {
    'nome': 'joao',
    'e-mail': 'joao@gmail.com',
    'saldo': 108
    },
    {
    'nome': 'Maria',
    'e-mail': 'maria@gmail.com',
    'saldo': 56.5
    },
    {
    'nome': 'JOSe',
    'e-mail': 'jose@email.com',
    'saldo': 567.53
    }]

print(f.filtrar_email(cadastro, 'hotmail'))
print(f.filtrar_email(cadastro, 'gmail'))
print(f.filtrar_email(cadastro, 'email'))

lista = [1, 4, 'A', 9.67, 'C', 5.7321]

print(f.filtrar_por_tipo(lista, str))
print(f.filtrar_por_tipo(lista, int))
print(f.filtrar_por_tipo(lista, float))
print(f.filtrar_por_tipo(lista, list))

lista_nomes = f.extrair_nomes(cadastro)
print(lista_nomes)

print(f.formatar_nomes(lista_nomes, 'CAIXA_ALTA'))
print(f.formatar_nomes(lista_nomes, 'CAIXA_BAIXA'))

lista_nomes = ['Maria', 'José', 'Joao', 'Pedro']
lista_emails = ['maria@email.com', 'jose@gmail.com', 'joao@gmail.com', 'pedro@email.com']

cadastro = f.criar_lista_cadastros(lista_nomes, lista_emails)
print(cadastro)

numeros_reais = [2.14, 3.12, 2.5, 3.1, 7.88]
print(f.transformar_real_para_inteiro(numeros_reais))

lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 4, 6, 8, 10]
lista3 = [1, 3, 5, 7, 9]
print(f.mapear_soma_do_maior_e_menor(lista1, lista2, lista3))

lista_original = [2, 7, 4, 9, 5, 3, 10, 7, 2]
print(f.criar_lista_numeros_iguais_correspondentes(lista_original))

strings = ['Bianca', 'Paula', 'Iago', 'Carolina', 'Mariana']
print(f.achar_maior_string(strings))

