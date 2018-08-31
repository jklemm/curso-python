# Faça um Programa que peça a temperatura em graus Farenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

# entrada de dados
farenheit = float(input('Informe a temperatura em graus Farenheit: '))

# processamento
celsius = 5 * (farenheit - 32) / 9
mensagem = '{} farenheit equivalem a {:.0f} celsius'.format(farenheit, celsius)

# saída de dados
print(mensagem)
