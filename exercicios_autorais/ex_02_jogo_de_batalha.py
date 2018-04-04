# Escreva um programa de batalha em turnos entre dois jogadores.
# Cada jogador vai informar seu nome, e cada jogador começa com 50 pontos de vida.
# Cada jogador pode escolher os golpes:
# 1 - Tapa na nuca (outro jogador perde 5 de vida)
# 2 - Dedo no olho (outro jogador perde 10 de vida)
# 3 - Chute de karatê (outro jogador perde 15 de vida)
# 4 - Ataque especial do losango invertido (outro jogador perde 25 de vida)
# O jogador que perder todos seus pontos de vida perde a batalha.

lista_de_jogadores = []
lista_de_golpes = [
    {
        'nome': 'Tapa na nuca',
        'dano': 5
    },
    {
        'nome': 'Dedo no olho',
        'dano': 10
    },
    {
        'nome': 'Chute de karatê',
        'dano': 15
    },
    {
        'nome': 'Ataque especial do losango invertido',
        'dano': 25
    }
]


def inicia():
    nome_jogador_1 = input('Informe o nome do Jogador 1: ')
    lista_de_jogadores.append({'nome': nome_jogador_1, 'vida': 50})

    nome_jogador_2 = input('Informe o nome do Jogador 2: ')
    lista_de_jogadores.append({'nome': nome_jogador_2, 'vida': 50})
    
    vez = 0
    while lista_de_jogadores[0]['vida'] > 0 and lista_de_jogadores[1]['vida'] > 0:
        print('É a vez do jogador {}'.format(lista_de_jogadores[vez]['nome']))
        print('Escolha um dos golpes abaixo:')
        print('1 - Tapa na nuca')
        print('2 - Dedo no olho')
        print('3 - Chute de karatê')
        print('4 - Ataque especial do losango invertido')

        golpe_escolhido = int(input('Digite o número do golpe escolhido: ')) - 1
        
        outro_jogador = 1 if vez == 0 else 0
        lista_de_jogadores[outro_jogador]['vida'] -= lista_de_golpes[golpe_escolhido]['dano']
        print('{} deu um {} em {}'.format(lista_de_jogadores[vez]['nome'], lista_de_golpes[golpe_escolhido]['nome'], lista_de_jogadores[outro_jogador]['nome']))
        print('{} ficou com {} pontos de vida'.format(lista_de_jogadores[outro_jogador]['nome'], lista_de_jogadores[outro_jogador]['vida']))

        vez = 1 if vez == 0 else 0

    jogador_vencedor = 0 if lista_de_jogadores[0]['vida'] > 0 else 1
    print('Jogador {} venceu a partida!'.format(lista_de_jogadores[jogador_vencedor]['nome']))
    
    print('Fim do jogo!')

if __name__ == '__main__':
    inicia()
