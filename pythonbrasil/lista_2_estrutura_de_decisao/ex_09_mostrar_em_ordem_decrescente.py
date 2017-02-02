"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""


def obter_numero_inteiro(msg):
    return int(input(msg))


def obter_numero_maior(numero_1, numero_2, numero_3):
    if numero_1 >= numero_2 and numero_1 >= numero_3:
        return numero_1
    elif numero_2 >= numero_1 and numero_2 >= numero_3:
        return numero_2
    else:
        return numero_3


def obter_numero_medio(numero_1, numero_2, numero_3):
    if numero_2 <= numero_1 <= numero_3 or numero_3 <= numero_1 <= numero_2:
        return numero_1
    elif numero_1 <= numero_2 <= numero_3 or numero_3 <= numero_2 <= numero_1:
        return numero_2
    else:
        return numero_3


def obter_numero_menor(numero_1, numero_2, numero_3):
    if numero_1 <= numero_2 and numero_1 <= numero_3:
        return numero_1
    elif numero_2 <= numero_1 and numero_2 <= numero_3:
        return numero_2
    else:
        return numero_3


def ordenar_em_ordem_decrescente(numero_1, numero_2, numero_3):
    numero_maior = obter_numero_maior(numero_1, numero_2, numero_3)
    numero_medio = obter_numero_medio(numero_1, numero_2, numero_3)
    numero_menor = obter_numero_menor(numero_1, numero_2, numero_3)

    return [numero_maior, numero_medio, numero_menor]


def ordena_tres_numeros_em_ordem_decrescente():
    numero_1 = obter_numero_inteiro('Informe o primeiro número: ')
    numero_2 = obter_numero_inteiro('Informe o segundo número: ')
    numero_3 = obter_numero_inteiro('Informe o terceiro número: ')

    numeros_ordenados = ordenar_em_ordem_decrescente(numero_1, numero_2, numero_3)

    print('Os números em ordem decrescente:', numeros_ordenados)


if __name__ == '__main__':
    print('+-----------------------------------------------------+')
    print('| Programa: Escreve três números em ordem decrescente |')
    print('+-----------------------------------------------------+')

    ordena_tres_numeros_em_ordem_decrescente()
