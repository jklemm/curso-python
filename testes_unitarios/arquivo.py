
def soma(a, b):
    return a + b


def potenciacao(a, b):
    return a ** b


def subtracao(a, b):
    return a - b


def todas_as_poltronas_estao_vendidas(poltronas):
    if 'Y' in poltronas:
        return True

    if '' in poltronas:
        return False
    else:
        return True
