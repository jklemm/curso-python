# Faça um Programa que peça dois números e imprima a soma.

# entrada de dados
numero_1 = int(input('Digite um número: ')) 
numero_2 = int(input('Digite mais um número: '))

# processamento
soma = numero_1 + numero_2
mensagem = '{} + {} = {}'.format(numero_1, numero_2, soma)

# saída de dados
print(mensagem)
