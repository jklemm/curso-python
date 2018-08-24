import random

numero_digitado = 0
numero_aleatorio = random.randint(0, 1000)
contar = 0
chances = 10

while numero_digitado != numero_aleatorio and chances > contar:

    contar += 1
    numero_digitado = int(input('Digite um numero de 0 a 1000: '))

    if numero_aleatorio == numero_digitado:
        print('Parabens, vc acertou!')
    else:

        if numero_digitado > numero_aleatorio:
            print('Errrrouuu! Tente um numero menor... Vc ainda tem {} chance(s)'.format(chances - contar))
        else:
            print('Errrrouuu! Tente um numero maior... Vc ainda tem {} chance(s)'.format(chances - contar))

        if contar == chances:
            print('Eh, nao foi dessa vez... O numero aleatorio era {}... Tente jogar novamente...'.format(numero_aleatorio))
