# Faça um Programa que converta metros para centímetros.

# entrada de dados
metros = float(input('Digite uma distância em metros: '))

# processamento
centimetros = int(metros * 100)
mensagem = '{} metros equivalem a {} centímetros'.format(metros, centimetros)

# saída de dados
print(mensagem)
