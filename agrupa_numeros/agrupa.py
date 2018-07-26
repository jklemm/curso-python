# Este problema foi utilizado em 183 Dojo(s).
# Dado uma lista de números inteiros, agrupe a 
# lista em um conjunto de intervalos
# Exemplo:
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
# Saída: [100-105], [110-111], [113-115], [150]


def agrupa(numeros):
    if not numeros:
        return ''

    resultado = numeros.split(', ')

    if len(resultado) == 1:
        return '[{}]'.format(resultado[0])
    else:
        return '[{}-{}]'.format(resultado[0],resultado[1])
