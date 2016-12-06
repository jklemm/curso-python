# coding: utf-8

print('=== Cálculo de IMC ===')

# meu editor estava reclamando que não inicializei as variáveis com valores
peso = 0
altura = 0

try:
    peso = input('Informe seu peso: ')
    # converte string para float e remove sinal negativo (não existe peso negativo)
    peso = abs(float(peso))
except ValueError:
    print('O peso informado {} é invalido!'.format(peso))
    # se o peso é inválido encerra o programa
    quit()

try:
    altura = input('Informe sua altura: ')
    # converte string para float e remove sinal negativo (não existe altura negativa)
    altura = abs(float(altura))
except ValueError:
    print('A altura informada {} é invalida!'.format(altura))
    # se a altura é inválida encerra o programa
    quit()

imc = peso / pow(altura, 2)

if imc < 17:
    situacao = 'Muito abaixo do peso'
elif 17 <= imc < 18.5:
    situacao = 'Abaixo do peso'
elif 18.5 <= imc < 25:
    situacao = 'Peso Normal'
elif 25 <= imc < 30:
    situacao = 'Acima do Peso'
elif 30 <= imc < 35:
    situacao = 'Obesidade I'
elif 35 <= imc < 40:
    situacao = 'Obesidade II (Severa)'
else:
    situacao = 'Obesidade III (Mórbida)'

print('Seu IMC é {:.2f}'.format(imc))
print('Você se enquadra na situação {}'.format(situacao))
