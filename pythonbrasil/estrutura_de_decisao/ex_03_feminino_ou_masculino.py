"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""


def pede_letra_ao_usuario(msg):
    return input(msg)


def obter_sexo_informado(letra):
    # upper - deixa a letra em MAIÚSCULO
    # strip - remove espaços em branco antes ou depois da letra
    letra = letra.upper().strip()
    if letra == 'M':
        return 'Masculino'
    elif letra == 'F':
        return 'Feminino'
    else:
        return 'Sexo indefinido'


def imprime_o_sexo_digitado():
    letra = pede_letra_ao_usuario('Informe uma letra que define um sexo: ')

    classificacao = obter_sexo_informado(letra)

    print('{} - {}'.format(letra, classificacao))


if __name__ == '__main__':
    print('+---------------------------------------+')
    print('| Programa: Verifica o sexo digitado    |')
    print('+---------------------------------------+')

    imprime_o_sexo_digitado()
