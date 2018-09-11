# 3 - Faça um Programa que leia 4 notas,
# mostre as notas e a média na tela.       


def obtem_notas():
    lista_notas = []

    for i in range(1, 5):
        nota = float(input('Digite a nota {}: '.format(i)))
        lista_notas.append(nota)
        lista_notas.pop() 

    return lista_notas


if __name__ == '__main__':
    notas = obtem_notas()

    total_das_notas = sum(notas)
    quantidade_de_notas = len(notas)
    media = total_das_notas / quantidade_de_notas

    print('A média das notas é {:.1f}'.format(media))
