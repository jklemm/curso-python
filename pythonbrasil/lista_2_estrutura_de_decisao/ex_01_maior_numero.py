"""
Faça um Programa que peça dois números e imprima o maior deles.
"""


def pede_numero_ao_usuario(msg):
    return float(input(msg))


def obter_o_maior_numero(num_1, num_2):
    # este é o chamado if ternário, faz o if em apenas uma linha
    maior_numero = num_1 if num_1 >= num_2 else num_2
    return maior_numero


def imprime_maior_numero():
    numero_1 = pede_numero_ao_usuario('Informe um número: ')
    numero_2 = pede_numero_ao_usuario('Informe mais um número: ')

    maior_numero = obter_o_maior_numero(numero_1, numero_2)

    print('O número {} é o maior número'.format(maior_numero))


if __name__ == '__main__':
    print('+---------------------------------------+')
    print('| Programa: Exibe maior de dois números |')
    print('+---------------------------------------+')

    imprime_maior_numero()
