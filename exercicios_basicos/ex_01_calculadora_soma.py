from exercicios_basicos.utils import obtem_numero_inteiro, efetua_soma


def inicia_calculadora_de_soma():
    numero_1 = obtem_numero_inteiro('Informe o primeiro numero: ')
    numero_2 = obtem_numero_inteiro('Informe o segundo numero: ')
    numero_3 = obtem_numero_inteiro('Informe o terceiro numero: ')

    resultado = efetua_soma(numero_1, numero_2, numero_3)

    print('A soma desses numeros eh: {}'.format(resultado))
    print('Ou seja, {} + {} + {} = {}'.format(numero_1, numero_2, numero_3, resultado))


if __name__ == '__main__':
    print('Calculadora que faz Soma')
    inicia_calculadora_de_soma()
