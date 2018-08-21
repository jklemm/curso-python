# Este problema foi utilizado em 183 Dojo(s).
# Dado uma lista de números inteiros, agrupe a 
# lista em um conjunto de intervalos
# Exemplo:
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
# Saída: [100-105], [110-111], [113-115], [150]


def agrupa(numeros_texto):
    if not numeros_texto:
        return ''

    lista_numeros_texto = numeros_texto.split(', ')
    resultado = ''

    if len(lista_numeros_texto) == 1:
        return '[{}]'.format(lista_numeros_texto[0])
    else:
        lista_numeros = converte_str_para_int(lista_numeros_texto)
        for indice, numero in enumerate(lista_numeros):
            try:
                if lista_numeros[indice + 1] == numero + 1:
                    continue
                else:
                    resultado += '[{}-{}]'.format(lista_numeros[indice], lista_numeros[indice+1])
            except IndexError:
                return resultado


def converte_str_para_int(lista):
    return list(map(int, lista))
