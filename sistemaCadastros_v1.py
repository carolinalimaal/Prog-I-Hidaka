def validarCadastros(cadastro: dict):
    try:
        if not cadastro['NOME'].isalpha():
            raise Exception('Nome inválido: contém caracteres especiais ou numéricos.')
        if not cadastro['NASC'].isnumeric() or len(cadastro['NASC']) != 4:
            raise Exception('Ano inválido.')
        if cadastro['SEXO'] not in 'MnFf':
            raise Exception('Sexo inválido.')
        if not cadastro['CPF'].isnumeric() or len(cadastro['CPF']) != 11:
            raise Exception('CPF inválido.')
        if not cadastro['RG'].isnumeric() or len(cadastro['RG']) != 7:
            raise Exception('RG inválido.')
        if not cadastro['TELEFONE'].isnumeric() or len(cadastro['TELEFONE']) != 9:
            raise Exception('Telefone inválido.')
        return True
    except Exception as errorMensagem:
        print(errorMensagem)
    return False



def cadastrar(listaCadastros: list):
    dictCadastro = {'NOME': input('NOME: '),
                   'NASC': input('ANO DE NASCIMENTO: '),
                   'SEXO': input('(M)/(F): ').upper(),
                   'CPF': input('CPF (Apenas os números): '),
                   'RG': input('RG (Apenas os números):: '),
                   'TELEFONE': input('TELEFONE (no padrão 9XXXXXXXX): ')}
    if validarCadastros(dictCadastro):
        listaCadastros.append(dictCadastro)


def listar(listaCadastros: list):
    if len(listaCadastros) == 0:
        print('Não há nenhum registro cadastrado!')
    for item in listaCadastros:
        print(f"""x=x=x=x=x=x=x=x=x=x=x=x
NOME: {item['NOME']}
ANO DE NASCIMENTO: {item['NASC']}
SEXO: {item['SEXO']}
CPF: {item['CPF']}
RG: {item['RG']}
TELEFONE: {item['TELEFONE']}
x=x=x=x=x=x=x=x=x=x=x=x""")

def main(listaCadastros: list):
    opcao = '1'
    while opcao in ['1', '2']:
        opcao = input("""
[1] CADASTRAR
[2] LISTAR
SUA ESCOLHA: """)
        print('')
        if opcao == '1':
            cadastrar(listaCadastros)
        if opcao == '2':
            listar(listaCadastros)
        else:
            print('FECHANDO PROGRAMA...')

cadastros = []
main(cadastros)
