# Em algumas empresas de desenvolvimento de software é comum, quando o prazo de entrega de uma aplicação está próximo, 
# a equipe passar algumas noites trabalhando. E como todo desenvolvedor também precisa se alimentar, eles sempre 
# pedem pizza nessas ocasiões. Só que sempre é uma briga para conseguir escolher os sabores das pizza de sabores que todos gostam.
# 
# Um dos membros da equipe, incomodado com as intermináveis discussões sobre o sabor a ser escolhido, resolveu desenvolver 
# um programa para facilitar essa escolha.
# 
# Para cada sabor de pizza disponível, cada um deve indicar uma nota para ele (nota 1, se a pessoa detesta o sabor e 
# nota 5 se a pessoa adora o sabor). Depois de processar esses dados, cada pessoa vai saber quais as pessoas que tem 
# o gosto mais parecido que o seu (e que provavelmente irá dividir uma pizza com você).
# 
# Por exemplo, para os dados a seguir, o Luca gostaria de saber quem ele deve convidar para dividir uma pizza com ele:
# 
# Renato = { Marguerita : 4, Quatro queijos : 5, Escarola : 4, Portuguesa : 5, Frango+Catupiry : 4, Napolitana : 3 }
# Marcelo = { Marguerita : 2, Quatro queijos : 2, Escarola : 1, Portuguesa : 3, Frango+Catupiry : 5, Napolitana : 2 }
# Lenon = { Marguerita : 4, Quatro queijos : 5, Escarola : 2, Portuguesa : 1, Frango+Catupiry : 1, Napolitana : 3 }
# Renata = { Marguerita : 4, Quatro queijos : 5, Escarola : 1, Portuguesa : 1, Frango+Catupiry : 3, Napolitana : 4 }
# Washington = { Marguerita : 1, Quatro queijos : 1, Escarola : 2, Portuguesa : 3, Frango+Catupiry : 4, Napolitana : 3 }
# Tino = { Marguerita : 1, Quatro queijos : 5, Escarola : 1, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }
# Luca = { Marguerita : 5, Quatro queijos : 4, Escarola : 3, Portuguesa : 4, Frango+Catupiry : 3, Napolitana : 2 }

# todo: reduzir o problema utilizando apenas 2 usuários e menos sabores

# todo: facilitar a solução utilizando 1 e 2 como False e 3 a 5 como True nas notas dos sabores
from itertools import product


def substitui_notas_por_true_e_false(usuarios):
    for usuario, sabores in usuarios.items():
        for sabor, nota in sabores.items():
            if nota >= 3:
                usuarios[usuario][sabor] = True
            else:
                usuarios[usuario][sabor] = False
    return usuarios


def verifica_se_combinam(sabores_do_usuario_1, sabores_do_usuario_2):
    quantidade_sabores_que_combinam = 0

    for sabor1, nota in sabores_do_usuario_1.items():
        nota_do_outro_usuario = sabores_do_usuario_2[sabor1]

        if nota is True and nota_do_outro_usuario is True:
            quantidade_sabores_que_combinam += 1

    if quantidade_sabores_que_combinam >= 3:
        return True
    else:
        return False


def main():
    usuarios = {
        'Renato': {'Marguerita': 4, 'Quatro queijos': 5,'Escarola': 4,'Portuguesa': 5, 'Frango+Catupiry': 4, 'Napolitana': 3},
        'Marcelo': {'Marguerita': 2, 'Quatro queijos': 2,'Escarola': 1,'Portuguesa': 3, 'Frango+Catupiry': 5, 'Napolitana': 2},
        'Lenon': {'Marguerita': 4, 'Quatro queijos': 5,'Escarola': 2,'Portuguesa': 1, 'Frango+Catupiry': 1, 'Napolitana': 3},
        'Renata': {'Marguerita': 4, 'Quatro queijos': 5,'Escarola': 1,'Portuguesa': 1, 'Frango+Catupiry': 3, 'Napolitana': 4},
        'Washington': {'Marguerita': 1, 'Quatro queijos': 1,'Escarola': 2,'Portuguesa': 3, 'Frango+Catupiry': 4,'Napolitana': 3},
        'Tino': {'Marguerita': 1, 'Quatro queijos': 5,'Escarola': 1,'Portuguesa': 4, 'Frango+Catupiry': 3, 'Napolitana': 2},
        'Luca': {'Marguerita': 5, 'Quatro queijos': 4,'Escarola': 3,'Portuguesa': 4, 'Frango+Catupiry': 3, 'Napolitana': 2},
    }

    print('Sabores das Pizzas')

    usuarios = substitui_notas_por_true_e_false(usuarios)

    usuario_desejado = input('Escreva o nome do usuário pra comparar sabores de pizza: ')

    sabores_que_usuario_desejado_gosta = usuarios[usuario_desejado] 

    for usuario, sabores in usuarios.items():
    
        if usuario == usuario_desejado:
            continue
    
        curtem = verifica_se_combinam(sabores_que_usuario_desejado_gosta , sabores)
    
        print('{} e {}: {} curtem os mesmos sabores!'.format(usuario_desejado, usuario, '' if curtem else 'NÃO'))
        

if __name__ == '__main__':
    main()
