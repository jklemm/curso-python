print('Cálculos envolvendo números inteiros e reais')

numero1 = int(input('Informe um número inteiro: '))

numero2 = int(input('Informe outro número inteiro: '))

numero3 = float(input('Informe um número real: '))

calculo1 = (numero1 * 2) * (numero2 / 2)

calculo2 = (numero1 * 3) + numero3

calculo3 = numero3 * numero3 * numero3  # ou pow(numero3, 3)

print('O produto do dobro do primeiro com metade do segundo = {:.2f}'.format(calculo1))

print('A soma do triplo do primeiro com o terceiro = {:.2f}'.format(calculo2))

print('O terceiro elevado ao cubo = {:.2f}'.format(calculo3))
