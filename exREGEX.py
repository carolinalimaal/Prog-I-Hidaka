import re


def verificarMuitoForte(senha):
    return re.search("[A-Z]", senha) and\
            re.search("[a-z]", senha) and\
            re.search("[0-9]", senha) and\
            re.search(".*[@#$%&+=].*[@#$%&+=].*[@#$%&+=]", senha) and\
            len(senha) >= 10

def verificarForte(senha):
    return re.search("[A-Z]", senha) and\
            re.search("[a-z]", senha) and\
            re.search("[0-9]", senha) and\
            re.search("[@#$%&+=]", senha) and\
            len(senha) >= 8

def verificarMedia(senha):
    return re.search("[A-Z]", senha) and\
            re.search("[a-z]", senha) and\
            re.search("[0-9]", senha) and\
            len(senha) >= 6

def verificarFraca(senha):
    return not(verificarMedia(senha)) and\
            len(senha) >= 6

def main():
    senhaUsuario = input('Digite sua senha: ')
    if verificarMuitoForte(senhaUsuario):
        print('Senha MUITO FORTE.')
    elif verificarForte(senhaUsuario):
        print('Senha FORTE.')
    elif verificarMedia(senhaUsuario):
        print('Senha MÉDIA')
    elif verificarFraca(senhaUsuario):
        print('Senha FRACA')
    else: 
        print('Senha INVÁLIDA')


main()
