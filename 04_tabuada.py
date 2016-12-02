# coding: utf-8

print('===== TABUADA =====')

# obter o número que se deseja gerar a tabuada
numero = input('Informe um número: ')

# converter o número de string para int
# se não converter, o cálculo matemático não funciona
numero = int(numero)

# gera a tabuada na tela, de 1 até 10
print('{} x {} = {}'.format(numero, 1, numero * 1))
print('{} x {} = {}'.format(numero, 2, numero * 2))
print('{} x {} = {}'.format(numero, 3, numero * 3))
print('{} x {} = {}'.format(numero, 4, numero * 4))
print('{} x {} = {}'.format(numero, 5, numero * 5))
print('{} x {} = {}'.format(numero, 6, numero * 6))
print('{} x {} = {}'.format(numero, 7, numero * 7))
print('{} x {} = {}'.format(numero, 8, numero * 8))
print('{} x {} = {}'.format(numero, 9, numero * 9))
print('{} x {} = {}'.format(numero, 10, numero * 10))
