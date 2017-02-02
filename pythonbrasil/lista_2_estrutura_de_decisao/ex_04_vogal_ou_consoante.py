"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""


def obter_letra_do_usuario(msg):
    return input(msg).lower().strip()


def is_vogal(letra):
    return letra in ('a', 'e', 'i', 'o', 'u')


def vogal_ou_consoante():
    letra = obter_letra_do_usuario('Informe uma letra: ')

    resultado = is_vogal(letra)

    if resultado:
        print('A letra informada é uma vogal')
    else:
        print('A letra informada não é uma vogal')


if __name__ == '__main__':
    print('+---------------------------------------+')
    print('| Programa: Vogal ou consoante          |')
    print('+---------------------------------------+')

    vogal_ou_consoante()
