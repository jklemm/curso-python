print('Calcula o dobro da área de um quadrado')

lateral = float(input('Informe o tamanho de um dos lados do quadrado: '))

area = lateral * lateral  # ou pow(lateral, 2)

dobro_da_area = area * 2

print('O dobro da área do quadrado {:.2f}'.format(dobro_da_area))
