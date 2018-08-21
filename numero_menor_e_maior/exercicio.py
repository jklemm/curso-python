
def detecta_maior_numero(numero_1, numero_2, numero_3):
    retorno = []

    if numero_1 == numero_2 == numero_3:
        retorno[0] = numero_1
        retorno[1] = numero_1

    elif numero_1 > numero_2 and numero_1 > numero_3:
        retorno[0] = numero_2 if numero_2 < numero_3 else numero_3
        retorno[1] = numero_1

    elif numero_2 > numero_1 and numero_2 > numero_3:
        retorno[0] = numero_1 if numero_1 < numero_3 else numero_3
        retorno[1] = numero_2

    else:
        retorno[0] = numero_1 if numero_1 < numero_2 else numero_2
        retorno[1] = numero_3

    return retorno       


if __name__ == '__main__':
    num_1 = int(input('Digite um número:'))
    num_2 = int(input('Digite mais um número:'))
    num_3 = int(input('Digite outro número:'))

    retorno = detecta_maior_numero(num_1, num_2, num_3)
    
    num_min = retorno[0]
    num_max = retorno[1]

    print('O menor é {} e o maior é {}'.format(num_min, num_max))
