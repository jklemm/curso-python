# coding: utf-8

print('=== Cálculo de IMC ===')

peso = input('Informe seu peso: ')
altura = input('Informe sua altura: ')

if peso and altura:

    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura * altura)

    if imc < 17:
        situacao = 'Muito abaixo do peso'
    elif imc >= 17 and imc < 18.5:
        situacao = 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        situacao = 'Peso Normal'
    elif imc >= 25 and imc < 30:
        situacao = 'Acima do Peso'
    elif imc >= 30 and imc < 35:
        situacao = 'Obesidade I'
    elif imc >= 35 and imc < 40:
        situacao = 'Obesidade II (Severa)'
    else:
        situacao = 'Obesidade III (Morbida)'

    print('Seu IMC é {}'.format(imc))
    print('Você se enquadra na situação: {}'.format(situacao))

else:

    print('O peso ou altura informados são inválidos!')
