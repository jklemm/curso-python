# coding: utf-8

print('Calcula o peso ideal')

altura = float(input('Informe sua altura: '))
sexo = input('Informe seu sexo (M)asculino ou (F)eminino: ')
peso = float(input('Informe o seu peso: '))

peso_ideal = 0

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    print('Sexo informado desconhecido!')
    quit()

situacao = ''

if int(peso) < int(peso_ideal):
    situacao = 'abaixo'
elif int(peso) == int(peso_ideal):
    situacao = 'dentro'
else:
    situacao = 'acima'

print('Seu peso ideal é {:.1f} kg'.format(peso_ideal))
print('Você está {} do peso ideal'.format(situacao))
