
# TODO: Autenticação com usuário e senha para acessar usa conta
# TODO: Manter o saldo atualizado em um arquivo JSON
# TODO: Manter um histórico de depósitos e saques e permitir gerar um extrato detalhado


def menu_deposito():
    return float(input('Digite o valor para depósito: R$ '))


def menu_saque():
    return float(input('Digite o valor para saque: R$ '))


def iniciar_caixa_eletronico():
    saldo = 0

    # FIXME: Verificar se usuário quer sair do sistema
    while True:
        print('Opções disponíves:')
        print('1 - Depósito')
        print('2 - Saque')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            saldo = fazer_deposito(saldo)
        elif opcao == 2:
            saldo = fazer_saque(saldo)

        print('Seu saldo é de: {}'.format(saldo))
        print('------------------------')


def fazer_saque(saldo):

    # TODO: Retornar a quantidade de notas de cada tamanho pro usuário
    # TODO: Informar dentro do programa a quantidade de notas de cada tamanho disponível

    valor_sacado = menu_saque()
    if valor_sacado <= saldo:
        saldo -= valor_sacado
        print('Valor R$ {} sacado!'.format(valor_sacado))
    else:
        print('Valor indisponível para saque!')
    return saldo


def fazer_deposito(saldo):
    valor_depositado = menu_deposito()
    saldo += valor_depositado
    print('Valor R$ {} depositado!'.format(valor_depositado))
    return saldo


if __name__ == '__main__':
    print('+-----------------------------+')
    print('| Programa: Caixa Eletrônico  |')
    print('+-----------------------------+')

    iniciar_caixa_eletronico()
