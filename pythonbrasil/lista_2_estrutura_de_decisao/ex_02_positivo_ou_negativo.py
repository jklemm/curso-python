"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""


def pede_numero_ao_usuario(msg):
    return float(input(msg))


def obter_positivo_ou_negativo(num):
    # este é o chamado if ternário, faz o if em apenas uma linha
    maior_numero = 'positivo' if num >= 0 else 'negativo'
    return maior_numero


def imprime_positivo_ou_negativo():
    numero = pede_numero_ao_usuario('Informe um número: ')

    sinal_do_numero = obter_positivo_ou_negativo(numero)

    print('O número {} é {}'.format(numero, sinal_do_numero))


if __name__ == '__main__':
    print('+---------------------------------------+')
    print('| Programa: Exibe positivo ou negativo  |')
    print('+---------------------------------------+')

    imprime_positivo_ou_negativo()
