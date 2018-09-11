# 3. Elabore um programa recursivo em C que calcule o n-ésimo termo da 
# sequência: 1, 2, 4, 8, 16, 32... .
# O termo deverá ser impresso na função main().

numero = 1


def multiplica(n):
    global numero

    if n == 0:
        return

    numero = numero * 2
    n -= 1
    
    multiplica(n)


if __name__ == '__main__':
    
    multiplica(50)

    print(numero)
