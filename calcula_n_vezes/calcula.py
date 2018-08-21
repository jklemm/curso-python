def eh_primo(numero):
    if numero == 1:
        return False

    for num in range(2, numero):
        if numero % num == 0:
            return False
    return True


if __name__ == '__main__':
    
    maximo = int(input('Digite um número inteiro: '))
    total = 0
    quantidade = 0

    for n in range(1, maximo + 1):
        if eh_primo(n):
            total += n
            quantidade += 1

    print('Achamos {} números primos!'.format(quantidade))
    print('O total é {}.'.format(total))
