# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi

# entrada de dados
raio = float(input('Digite o raio do círculo: '))

# processamento
area = pi * pow(raio, 2)
mensagem = 'A área do círculo é {0:.3f}'.format(area)

# saída de dados
print(mensagem)
