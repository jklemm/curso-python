# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, utilizando 
# as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# entrada de dados
sexo = input('Informe Masculino (M) ou Feminino (F): ')
altura = float(input('Informe sua altura (em metros): '))

# processamento
if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    resposta = 'O peso ideal para um homem de {}m de altura é {:.2f} quilos'.format(altura, peso_ideal)
else:
    peso_ideal = (62.1 * altura) - 44.7
    resposta = 'O peso ideal para uma mulher de {}m de altura é {:.2f} quilos'.format(altura, peso_ideal)

# saída de dados
print(resposta)
