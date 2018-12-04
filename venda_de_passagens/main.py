# * Criar um programa que gerencie a venda e ocupação de poltronas para uma viagem de ônibus.
# Crianças (<5 anos) e idosos (>65 anos) pagam apenas 50% da passagem.
# * Mantenha o programa em execução até que o operador decida não vender mais passagens.
# * O programa não pode permitir que duas passagens para a mesma poltrona sejam vendidas.
# * O programa deve cancelar a viagem se menos de 50% das passagens forem
# vendidas quando o operador encerrar as vendas.
# * Utilize 4 vetores para armazenar a ocupação para as poltronas - um vetor para cada fileira
# de poltronas, sendo 2 para janela e 2 para o corredor.
# * Ao final da execução, informe o faturamento total das vendas (em Reais), caso a viagem seja confirmada.
# * Ao final da execução, informe se a viagem foi cancelada ou não.

# Declaração de Constantes
VENDER_PASSAGEM = 1
VER_POLTRONAS = 2
FINALIZAR_VENDAS = 3
SAIR = 4
OPCAO_JANELA = 'J'
OPCAO_CORREDOR = 'C'
OPCAO_DIREITA = 'D'
OPCAO_ESQUERDA = 'E'
NUMERO_PASSAGENS_DISPONIVEIS = 40
NUMERO_ASSENTOS_POR_FILA = NUMERO_PASSAGENS_DISPONIVEIS // 4
VALOR_PASSAGEM = 100


def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def poltrona_ja_esta_vendida(poltrona):
    return True if poltrona == 'X' else False


def menu_passagem():
    print('+-------------------------------------+')
    print('| CONTROL-VIAGENS: VENDA DE PASSAGENS |')
    print('+-------------------------------------+')
    print('[ 1 ] Vender passagem')
    print('[ 2 ] Ver poltronas')
    print('[ 3 ] Finalizar Vendas')
    print('[ 4 ] Sair')
    print('+-------------------------------------+')
    return int(input('Informe sua opção: '))


def todas_poltronas_estao_vendidas(poltronas):
    if '' not in poltronas:
        return True
    else:
        return False


def busca_posicoes_livres(poltronas):
    lista_posicoes_livres = []
    for indice, poltrona in enumerate(poltronas, start=1):
        if not poltrona_ja_esta_vendida(poltrona):
            lista_posicoes_livres.append(indice)
    return lista_posicoes_livres


def exibe_posicoes_livres(poltronas_livres):
    posicoes_livres = ' - '.join(str(numero_poltrona) for numero_poltrona in poltronas_livres)
    print(posicoes_livres)


def opcao_vender_passagem(pass_meia, pass_inteira, pol_janela_direita, pol_corredor_direita, pol_janela_esquerda, pol_corredor_esquerda, total_vendido):
    while total_vendido <= NUMERO_PASSAGENS_DISPONIVEIS:
        print('Vender passagem')
        idade = obter_idade()
        paga_meia = idade < 5 or idade > 65
        if paga_meia:
            pass_meia += 1
        else:
            pass_inteira += 1

        print('Escolha sua poltrona: ')
        opcao_ver_poltronas()

        opcao_janela_ou_corredor = input('Digite opção Janela [ J ] ou Corredor [ C ]?: ').upper()
        if opcao_janela_ou_corredor == OPCAO_JANELA:

            opcao_direira_ou_esquerda = input('Janela direita [ D ] ou esquerda [ E ]: ').upper()
            if opcao_direira_ou_esquerda == OPCAO_DIREITA:
                vender_uma_passagem(pol_janela_direita, total_vendido)
            elif opcao_direira_ou_esquerda == OPCAO_ESQUERDA:
                vender_uma_passagem(pol_janela_esquerda, total_vendido)
            else:
                print('Opção inválida!')

        elif opcao_janela_ou_corredor == OPCAO_CORREDOR:

            opcao_direira_ou_esquerda = input('Corredor direita [ D ] ou esquerda [ E ]: ').upper()
            if opcao_direira_ou_esquerda == OPCAO_DIREITA:
                vender_uma_passagem(pol_corredor_direita, total_vendido)
            elif opcao_direira_ou_esquerda == OPCAO_ESQUERDA:
                vender_uma_passagem(pol_corredor_esquerda, total_vendido)
            else:
                print('Opção inválida!')

        else:
            print('Opção inválida!')

        if total_vendido == 12:
            print('\n***** Todas as passagens foram vendidas! *****\n')
            break

        comprar_mais = input('Deseja vender outra passagem? [S/N]: ').upper()
        if comprar_mais == 'S':
            limpar_tela()
            continue
        else:
            break


def obter_idade():
    idade_valida = False
    idade = 0
    while not idade_valida:
        idade = int(input('Qual a idade do passageiro?: '))
        if 0 <= idade <= 120:
            idade_valida = True
        else:
            print('Idade inválida, digite novamente!')
    return idade


def vender_uma_passagem(poltronas, total_passagens):
    if todas_poltronas_estao_vendidas(poltronas):
        print('Todos os lugares estão ocupados!')

    print('Posições livres:')
    lista_posicoes_livres = busca_posicoes_livres(poltronas)
    exibe_posicoes_livres(lista_posicoes_livres)

    finalizou_compra = False
    while not finalizou_compra:
        polcompra = int(input('\nDigite o número da poltrona desejada: '))
        if polcompra in lista_posicoes_livres:
            poltronas[polcompra - 1] = 'X'
            total_passagens += 1
            finalizou_compra = True
        else:
            print('Opção invalida! Escolha uma poltrona válida!')
            finalizou_compra = False

    print('\nPassagem vendida com sucesso!\n')


def opcao_ver_poltronas():
    print('Lugares vagos [ ] - Lugares ocupados [X]\n')
    print('   /__ _ ', end='')
    for poltrona in poltronas_janela_direita:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print(' \  : Janela Direita')

    print('  |   |  ', end='')
    for poltrona in poltronas_corredor_direita:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print('  | : Corredor Direita')

    print('  | __|_ ', end='')
    for poltrona in poltronas_corredor_esquerda:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print('  | : Corredor Esquerda')

    print('   \     ', end='')
    for poltrona in poltronas_janela_esquerda:
        print('[{}]'.format(poltrona if poltrona else ' '), end='')
    print(' /  : Janela Esquerda')


def opcao_finalizar_vendas():
    print('Finalizar Vendas')
    # TODO: Soma meias e inteiras e verifica se 50% ou mais foi vendido, senão a viagem é cancelada
    # TODO: Multiplica a qtd de meia pelo valor da meia entrada
    # TODO: Multiplica a qtd de inteiras pelo valor da entrada inteira
    # TODO: Soma e informa o total vendido


if __name__ == '__main__':
    # Declaração de Variáveis
    passagem_meia = 0
    passagem_inteira = 0
    poltronas_janela_direita = [''] * NUMERO_ASSENTOS_POR_FILA
    poltronas_corredor_direita = [''] * NUMERO_ASSENTOS_POR_FILA
    poltronas_janela_esquerda = [''] * NUMERO_ASSENTOS_POR_FILA
    poltronas_corredor_esquerda = [''] * NUMERO_ASSENTOS_POR_FILA
    total_vendido = 0

    while True:
        opcao_menu = menu_passagem()

        if opcao_menu == VENDER_PASSAGEM:
            opcao_vender_passagem(
                passagem_meia,
                passagem_inteira,
                poltronas_janela_direita,
                poltronas_corredor_direita,
                poltronas_janela_esquerda,
                poltronas_corredor_esquerda,
                total_vendido
            )

        elif opcao_menu == VER_POLTRONAS:
            print('Ver poltronas\n')
            opcao_ver_poltronas()

        elif opcao_menu == FINALIZAR_VENDAS:
            opcao_finalizar_vendas()
            break

        elif opcao_menu == SAIR:
            break
