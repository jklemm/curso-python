def inicia_cadastro(alunos):
    print('Escolha a opção:')
    print('1 - Listar alunos')
    print('2 - Cadastrar aluno')
    print('3 - Buscar aluno')
    opcao = int(input('Opção: '))

    if opcao == 1:
        listar_alunos(alunos)
    elif opcao == 2:
        cadastrar_aluno(alunos)
    elif opcao == 3:
        buscar_aluno(alunos)


def listar_alunos(alunos):
    if len(alunos) == 0:
        print('lista vazia!')
    else:
        print('Exibindo a lista de alunos:')
        for aluno in alunos:
            print(aluno)


def cadastrar_aluno(alunos):
    aluno = input('Informe o nome do aluno: ')
    alunos.append(aluno)


def buscar_aluno(alunos):
    nome_procurado = input('Informe o nome exato do aluno: ')
    for indice, aluno in enumerate(alunos, start=0):
        if aluno.lower().strip() == nome_procurado.lower().strip():
            print('O indice do aluno {} é {}'.format(nome_procurado, indice))
            return

    print('Aluno não encontrado!')


if __name__ == '__main__':
    lista_de_alunos = []
    while True:
        inicia_cadastro(lista_de_alunos)

