# Crie um programa de autenticação de usuários
# Logo após executar, o programa dá duas possibilidades: "Cadastre-se" ou 
# "Efetuar Login"
# Em Cadastre-se, o usuário vai informar o nome, e-mail e senha, logo após 
# volta pra tela inicial
# Em Efetuar login, o usuário precisa informar o usuário e senha
# - Se o usuário e senha estiverem corretos, informar "Olá {nome_do_usuario}! 
# Você está logado!".. E permite efetuar o Logout, voltando pra tela inicial.
# - Se o usuário não existir ou a senha estiver incorreta, informar "Usuário 
# ou senha incorretos", e deve pedir o usuário e senha novamente.
# Bônus: Armazenar os dados do usuário em um arquivo JSON, dessa forma, mesmo 
# após fechar o programa, o usuário continuará lá cadastrado.
import json

import codecs

lista_de_usuarios = []


def carregar_usuarios_do_arquivo_json():
    arquivo_usuarios = codecs.open('usuarios.json', encoding='utf-8')
    usuarios_texto = arquivo_usuarios.read()
    usuarios_json = json.loads(usuarios_texto)
    return usuarios_json


def gravar_usuarios_no_arquivo_json():
    with open('usuarios.json', 'w') as arquivo_usuarios:
        usuarios_texto = json.dumps(lista_de_usuarios)
        arquivo_usuarios.write(usuarios_texto)


def tela_cadastre_se():
    print('+-------------------------------+')
    print('| CADASTRE-SE                   |')
    print('+-------------------------------+')
    nome = input('Informe seu nome: ')
    email = input('Informe seu e-mail: ')
    senha = input('Informe uma senha: ')
    novo_usuario = {'nome': nome, 'email': email, 'senha': senha}
    lista_de_usuarios.append(novo_usuario)
    gravar_usuarios_no_arquivo_json()
    tela_inicial()


def email_e_senha_corretos(email, senha):
    for usuario in lista_de_usuarios:
        if email == usuario['email']:
            if senha == usuario['senha']:
                return True
            else:
                break
    return False


def tela_logado():
    print('+-------------------------------+')
    print('| SUCESSO! VOCÊ ESTÁ LOGADO     |')
    print('+-------------------------------+')
    print('1 - Sair')
    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        tela_inicial()
    else:
        print('Opção Inválida! Escolha novamente')
        tela_logado()


def tela_efetuar_login():
    print('+-------------------------------+')
    print('| EFETUAR LOGIN                 |')
    print('+-------------------------------+')
    email = input('Informe seu e-mail: ')
    senha = input('Informe uma senha: ')
    if email_e_senha_corretos(email, senha):
        tela_logado()
    else:
        print('+-------------------------------+')
        print('| USUÁRIO OU SENHA INCORRETOS   |')
        print('+-------------------------------+')
        tela_inicial()


def tela_inicial():
    print('+-------------------------------+')
    print('| TELA INICIAL                  |')
    print('+-------------------------------+')
    print('1 - Cadastre-se')
    print('2 - Efetuar login')
    print('3 - Encerrar programa')
    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        tela_cadastre_se()
    elif opcao == 2:
        tela_efetuar_login()
    elif opcao == 3:
        exit(0)
    else:
        print('Opção Inválida! Escolha novamente')
        tela_inicial()


if __name__ == '__main__':
    lista_de_usuarios = carregar_usuarios_do_arquivo_json()
    tela_inicial()
