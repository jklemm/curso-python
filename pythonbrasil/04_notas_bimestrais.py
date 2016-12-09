print('Calcula notas bimestrais')

print('Informe suas quatro notas bimestrais')

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('A média das notas é {:.1f}'.format(media))
