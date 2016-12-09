print('Calcula o salário mensal\n')

valor_hora = float(input('Informe quanto você ganha por hora: R$ '))
quantidade_horas = float(input('Informe o número de horas trabalhadas no mês: '))

salario_bruto = valor_hora * quantidade_horas
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato

print('')
print('+ Salário Bruto   : R$ {:8.2f}'.format(salario_bruto))
print('- IR (11%)        : R$ {:8.2f}'.format(imposto_de_renda))
print('- INSS (8%)       : R$ {:8.2f}'.format(inss))
print('- Sindicato (5%)  : R$ {:8.2f}'.format(sindicato))
print('= Salário Liquido : R$ {:8.2f}'.format(salario_liquido))
