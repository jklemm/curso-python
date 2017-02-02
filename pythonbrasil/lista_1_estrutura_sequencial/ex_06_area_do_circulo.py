import math

print('Calcula a área do círculo')

raio = float(input('Informe o raio de um círculo: '))

area = math.pi * pow(raio, 2)

print('A área deste círculo é {:.2f}'.format(area))
