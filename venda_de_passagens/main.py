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
NUMERO_PASSAGENS_DISPONIVEIS = 12
NUMERO_ASSENTOS_POR_FILA = NUMERO_PASSAGENS_DISPONIVEIS // 4


def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_poltronas():
    print('Lugares vagos [ ] - Lugares ocupados [X]\n')
    print('                     /__ _ [ ][ ][ ] \  : Janela Direita')
    print('Frente do ônibus <- |   |  [ ][ ][ ]  | : Janela Esquerda')
    print('                    | __|_ [ ][ ][ ]  | : Corredor Direita')
    print('                     \     [ ][ ][ ] /  : Corredor Esquerda')


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


def mostra_posicoes_livres(poltronas):
    posicoes_livres = ' - '.join(str(indice) if not poltrona else poltrona
                                 for indice, poltrona in enumerate(poltronas, start=1))
    print(posicoes_livres)


def opcao_vender_passagem(pass_meia, pass_inteira, pol_janela_direita, pol_corredor_direita, pol_janela_esquerda, pol_corredor_esquerda, total_vendido):
    while total_vendido <= NUMERO_PASSAGENS_DISPONIVEIS:
        print('Vender passagem')
        idade = int(input('Qual a idade do passageiro?: '))
        paga_meia = idade < 5 or idade > 65
        if paga_meia:
            pass_meia += 1
        else:
            pass_inteira += 1

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


def vender_uma_passagem(poltronas, total_passagens):
    if todas_poltronas_estao_vendidas(poltronas):
        print('Todos os lugares estão ocupados!')

    print('Posições livres:')
    mostra_posicoes_livres(poltronas)

    polcompra = int(input('\nDigite o número da poltrona desejada: '))
    if polcompra > 3:
        print('Opção invalida!')

    poltronas[polcompra - 1] = 'X'
    total_passagens += 1


def opcao_ver_poltronas():
    print('Ver poltronas')


def opcao_finalizar_vendas():
    print('Finalizar Vendas')


def opcao_sair():
    print('Sair')


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
            opcao_ver_poltronas()

        elif opcao_menu == FINALIZAR_VENDAS:
            opcao_finalizar_vendas()

        elif opcao_menu == SAIR:
            opcao_sair()
