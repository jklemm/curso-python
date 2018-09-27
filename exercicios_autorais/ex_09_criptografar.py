# Crie um programa para criptografar uma mensagem
# Desta forma, você pode escrever uma mensagem e passar para seu colega
# E mesmo que alguém pegue a mensagem no caminho não vai entender o conteúdo
# Para criptografar, substitua as letras por números, seguindo a tabela abaixo:

# A a -> 01
# B b -> 02
# C c -> 03
# D d -> 04
# ...
# Z z -> 26
# " " -> 27
# 0   -> 28
# ...
# 9   -> 37

# forma de chamar no console:
# python ex_09_criptografar.py 'cifrar' 'teste'
# python ex_09_criptografar.py 'decifrar' '010203040506070809'

import sys

alfabeto = {
    'A': '01', 'B': '02', 'C': '03', 'D': '04', 'E': '05', 'F': '06', 'G': '07',
    'H': '08', 'I': '09', 'J': '10', 'K': '11', 'L': '12', 'M': '13', 'N': '14',
    'O': '15', 'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20', 'U': '21',
    'V': '22', 'W': '23', 'X': '24', 'Y': '25', 'Z': '26', ' ': '27', '0': '28',
    '1': '29', '2': '30', '3': '31', '4': '32', '5': '33', '6': '34', '7': '35',
    '8': '36', '9': '37', '!': '38', '?': '39', ',': '40', '.': '41',
}


def busca_chave_por_valor(dicionario, valor_procurado):
    for chave, valor in dicionario.items():
        if valor == valor_procurado:
            return chave
    return ''


def cifrar(texto):
    retorno = ''

    texto = texto.upper()
    for letra in texto:
        retorno += alfabeto.get(letra, '**')

    return retorno


def decifrar(texto_cifrado):
    retorno = ''

    lista_texto = []
    for (char1, char2) in zip(texto_cifrado[0::2], texto_cifrado[1::2]):
        lista_texto.append('{}{}'.format(char1, char2))

    for numero in lista_texto:
        retorno += busca_chave_por_valor(alfabeto, numero)

    return retorno


if __name__ == '__main__':
    tipo = sys.argv[1]
    texto = sys.argv[2]
    
    if tipo == 'cifrar':
        print(cifrar(texto))
    elif tipo == 'decifrar':
        print(decifrar(texto))
