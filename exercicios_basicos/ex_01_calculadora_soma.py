
def obtem_numero_inteiro(texto):
    return int(input(texto))


def efetua_soma(num_1=0, num_2=0, num_3=0):
    return num_1 + num_2 + num_3


def obtem_tres_numeros_inteiros():
    numero_1 = obtem_numero_inteiro('Informe o primeiro numero: ')
    numero_2 = obtem_numero_inteiro('Informe o segundo numero: ')
    numero_3 = obtem_numero_inteiro('Informe o terceiro numero: ')
    return numero_1, numero_2, numero_3


def apresenta_resultados(numero_1, numero_2, numero_3, resultado):
    print('A soma desses numeros eh: {}'.format(resultado))
    print('Ou seja, {} + {} + {} = {}'.format(numero_1, numero_2, numero_3, resultado))


if __name__ == '__main__':
    print('Calculadora que faz Soma')

    numero_1, numero_2, numero_3 = obtem_tres_numeros_inteiros()
    resultado = efetua_soma(numero_1, numero_2, numero_3)
    apresenta_resultados(numero_1, numero_2, numero_3, resultado)
