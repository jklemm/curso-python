"""
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""


def obter_nota_do_aluno(msg):
    return float(input(msg))


def calcula_media_das_notas(n1, n2):
    return (n1 + n2) / 2


def obter_classificacao_do_aluno(media):
    if media < 7:
        return 'Reprovado'
    elif media < 10:
        return 'Aprovado'
    else:
        return 'Aprovado com Distinção'


def verifica_situacao_do_aluno():
    nota_1 = obter_nota_do_aluno('Informe a nota 1 do aluno: ')
    nota_2 = obter_nota_do_aluno('Informe a nota 2 do aluno: ')

    media = calcula_media_das_notas(nota_1, nota_2)
    classificacao = obter_classificacao_do_aluno(media)

    print('A média do aluno foi', media, 'e ele está', classificacao)


if __name__ == '__main__':
    print('+---------------------------------------+')
    print('| Programa: Verifica situação do aluno  |')
    print('+---------------------------------------+')

    verifica_situacao_do_aluno()
