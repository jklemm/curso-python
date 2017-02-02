"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""


def obter_numero_inteiro(msg):
    return int(input(msg))


def obter_maior_numero(numero_1, numero_2, numero_3):
    if numero_1 >= numero_2 and numero_1 >= numero_3:
        return numero_1
    elif numero_2 >= numero_1 and numero_2 >= numero_3:
        return numero_2
    else:
        return numero_3


def obter_menor_numero(numero_1, numero_2, numero_3):
    if numero_1 <= numero_2 and numero_1 <= numero_3:
        return numero_1
    elif numero_2 <= numero_1 and numero_2 <= numero_3:
        return numero_2
    else:
        return numero_3


def verifica_maior_e_menor_de_tres_numeros():
    numero_1 = obter_numero_inteiro('Informe o primeiro número: ')
    numero_2 = obter_numero_inteiro('Informe o segundo número: ')
    numero_3 = obter_numero_inteiro('Informe o terceiro número: ')

    maior_numero = obter_maior_numero(numero_1, numero_2, numero_3)
    menor_numero = obter_menor_numero(numero_1, numero_2, numero_3)

    print('O maior número é', maior_numero, 'e o menor número é', menor_numero)


if __name__ == '__main__':
    print('+--------------------------------------------------+')
    print('| Programa: Verifica maior e menor de três números |')
    print('+--------------------------------------------------+')

    verifica_maior_e_menor_de_tres_numeros()
