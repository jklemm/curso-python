
def tabuada(numero):
    resultados = []
    for contador in range(1, 11):
        multiplicador = '{} x {} = {}'.format(numero, contador, numero * contador)
        resultados.append(multiplicador)
    return resultados
