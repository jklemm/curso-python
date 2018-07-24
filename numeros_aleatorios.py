from random import randint


def processa_numeros_aleatorios(num_desejados=6, num_minimo=0, num_maximo=100):
    num_aleatorios = []

    for i in range(0, num_desejados):
        numero = randint(num_minimo, num_maximo)
        while numero in num_aleatorios:
            numero = randint(num_minimo, num_maximo)
        num_aleatorios.append(numero)

    return num_aleatorios


def formata_numeros(numeros):
    return ', '.join(str(numero) for numero in numeros)


if __name__ == '__main__':
    numeros_desejados = int(input('Digite a quantidade de números desejados: '))
    numero_minimo = int(input('Digite o número mínimo: '))
    numero_maximo = int(input('Digite o número máximo: '))

    numeros_aleatorios = processa_numeros_aleatorios(numeros_desejados, numero_minimo, numero_maximo)

    print(formata_numeros(numeros_aleatorios))
