print 'Calculadora que faz 2 operacoes'

operacao = raw_input('Informe a operacao desejada (1 - Soma, 2 - Subtracao): ')

if operacao in ('1', '2'):

    numero1 = raw_input('Informe o primeiro numero: ')

    numero2 = raw_input('Informe o segundo numero: ')

    numero3 = raw_input('Informe o terceiro numero: ')

    if operacao == '1':

        resultado = int(numero1) + int(numero2) + int(numero3)

        print 'A soma desses numeros eh: {}'.format(resultado)

        print 'Ou seja, {} + {} + {} = {}'.format(numero1, numero2, numero3, resultado)

    elif operacao == '2':

        resultado = int(numero1) - int(numero2) - int(numero3)

        print 'A subtracao desses numeros eh: {}'.format(resultado)

        print 'Ou seja, {} - {} - {} = {}'.format(numero1, numero2, numero3, resultado)

else:
    print 'Esta operacao nao existe, redigite outra..'
