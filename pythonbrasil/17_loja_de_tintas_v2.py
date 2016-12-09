# coding: utf-8
from math import ceil

print('Loja de tintas\n')

area_a_ser_pintada = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

um_litro_pinta = 6
quantidade_de_uma_lata = 18
preco_de_cada_lata = 80.00
quantidade_de_um_galao = 3.6
preco_de_cada_galao = 25.00


litros_necessarios = area_a_ser_pintada / um_litro_pinta

latas_necessarias = int(ceil(litros_necessarios / quantidade_de_uma_lata))
valor_total_para_latas = latas_necessarias * preco_de_cada_lata

galoes_necessarios = int(ceil(litros_necessarios / quantidade_de_um_galao))
valor_total_para_galoes = galoes_necessarios * preco_de_cada_galao

print('')
print('=== SE VOCÊ COMPRAR LATAS ===')
print('Você vai precisar de {} latas de tinta a serem compradas'.format(latas_necessarias))
print('Preço total de latas: R$ {:.2f}'.format(valor_total_para_latas))

print('')
print('=== SE VOCÊ COMPRAR GALÕES ===')
print('Você vai precisar de {} galões de tinta a serem comprados'.format(galoes_necessarios))
print('Preço total de galões: R$ {:.2f}'.format(valor_total_para_galoes))

print('')
print('=== SE VOCÊ COMPRAR MISTO DE GALÕES E LATAS ===')

if litros_necessarios < (quantidade_de_um_galao * 3):
    galoes_necessarios = litros_necessarios / quantidade_de_um_galao
    valor_total_para_galoes = galoes_necessarios * preco_de_cada_galao
    print('Você vai precisar de {} galões de tinta a ser comprado'.format(galoes_necessarios))
    print('Preço total de galões: R$ {:.2f}'.format(valor_total_para_galoes))
else:
    latas_necessarias = litros_necessarios / quantidade_de_uma_lata
    valor_total_para_latas = latas_necessarias * preco_de_cada_lata
    print('Você vai precisar de {} latas de tinta a ser comprado'.format(latas_necessarias))
    print('Preço total de latas: R$ {:.2f}'.format(valor_total_para_galoes))
