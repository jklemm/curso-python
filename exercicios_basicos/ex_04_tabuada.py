
def tabuada(numero):
    for contador in range(1, 31):
        print('{} x {} = {}'.format(numero, contador, numero * contador))


if __name__ == '__main__':
    print('===== TABUADA =====')

    numero_obtido = int(input('Informe um número: '))

    tabuada(numero_obtido)
