# coding: utf-8

print('Calcula o salário mensal')

valor_hora = float(input('Informe quanto você ganha por hora: R$ '))

quantidade_horas = float(input('Informe o número de horas trabalhadas no mês: '))

salario = valor_hora * quantidade_horas

print('O total do salário neste mês foi R$ {:.2f}'.format(salario))
