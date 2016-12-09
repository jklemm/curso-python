from math import ceil

print('Loja de tintas\n')

area_a_ser_pintada = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

um_litro_pinta = 3
quantidade_de_uma_lata = 18
preco_de_cada_lata = 80.00

litros_necessarios = area_a_ser_pintada / um_litro_pinta

latas_necessarias = int(ceil(litros_necessarios / quantidade_de_uma_lata))

valor_total = latas_necessarias * preco_de_cada_lata

print('Você vai precisar de {} latas de tinta a serem compradas'.format(latas_necessarias))
print('Preço total: R$ {:.2f}'.format(valor_total))
