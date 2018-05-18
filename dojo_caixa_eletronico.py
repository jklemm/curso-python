# Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico.
# Os requisitos básicos são os seguintes:
# 
# Entregar o menor número de notas;
# É possível sacar o valor solicitado com as notas disponíveis;
# Saldo do cliente infinito;
# Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
# Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
# Exemplos:
# 
# Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
# Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.


def inicializa_quantidade_de_notas_com_zero(notas, valores_das_notas):
    for valor_da_nota in valores_das_notas:
        notas[valor_da_nota] = 0


def obtem_valor_valido():
    valor_desejado = 0
    valor_valido = False
    while not valor_valido:
        valor_desejado = int(input('Informe o valor desejado (múltiplo de 5): '))
        valor_valido = valor_desejado % 5 == 0
        if not valor_valido:
            print('Valor Inválido! Digite um valor que é múltiplo de 5!')
    return valor_desejado


def divide_valor_desejado_em_notas(notas, valor_desejado, valores_das_notas):
    for tamanho_de_nota in valores_das_notas:
        while valor_desejado >= tamanho_de_nota:
            valor_desejado -= tamanho_de_nota
            notas[tamanho_de_nota] += 1
    return notas


def imprime_quantidade_de_notas(notas, valores_das_notas):
    for tamanho_de_nota in valores_das_notas:
        if notas[tamanho_de_nota] > 0:
            print('Notas de {}: {}'.format(tamanho_de_nota, notas[tamanho_de_nota]))


def main():
    print('Caixa Eletrônico da MP')
    print('Bem vindo.')

    valores_das_notas = (100, 50, 20, 10, 5)
    notas = {}
    inicializa_quantidade_de_notas_com_zero(notas, valores_das_notas)

    valor_desejado = obtem_valor_valido()

    notas = divide_valor_desejado_em_notas(notas, valor_desejado, valores_das_notas)

    imprime_quantidade_de_notas(notas, valores_das_notas)


if __name__ == '__main__':
    main()
