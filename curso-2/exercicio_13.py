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
    constante = 72.7
    decremento = 58
    genero = 'um homem'
else:
    constante = 62.1
    decremento = 44.7
    genero = 'uma mulher'

peso_ideal = constante * altura - decremento
resposta = 'O peso ideal para {} de {}m de altura é {:.2f} quilos'.format(genero, altura, peso_ideal)

# saída de dados
print(resposta)
