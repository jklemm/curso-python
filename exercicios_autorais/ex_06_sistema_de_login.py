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

lista_de_usuarios = []


def tela_cadastre_se():
    print('tela_cadastre_se')
    pass


def usuario_e_senha_corretos(usuario, senha):
    pass


def tela_logado():
    pass


def tela_fracasso():
    pass


def tela_efetuar_login():
    print('tela_efetuar_login')
    usuario = ''
    senha = ''
    if usuario_e_senha_corretos(usuario, senha):
        tela_logado()
    else:
        tela_fracasso() 


def tela_inicial():
    print('Tela inicial')
    print('1 - Cadastre-se')
    print('2 - Efetuar login')
    opcao = int(input('Escolha sua opção: '))

    if opcao == 1:
        tela_cadastre_se()
    elif opcao == 2:
        tela_efetuar_login()
    else:
        print('Opção Inválida! Escolha novamente')
        tela_inicial()


if __name__ == '__main__':
    tela_inicial()
