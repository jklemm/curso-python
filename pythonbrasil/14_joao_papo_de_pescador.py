# coding: utf-8

print('Calcula peso de peixes excedente')

multa_por_quilo_excedente = 4.00

peso = float(input('Informe o peso total de peixes pescados: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * multa_por_quilo_excedente
    excesso = multa
else:
    excesso = 'ZERO'
    multa = 'ZERO'

print('Excesso: {}'.format(excesso))
print('Multa: {}'.format(multa))
