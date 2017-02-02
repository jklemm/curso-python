
def obter_resposta(pergunta):
    resposta = input(pergunta).lower().strip()
    if resposta == 'sim':
        return 1
    elif resposta == 'talvez':
        return 0.5
    else:
        return 0


def obter_classificacao(nivel):
    if nivel < 2:
        texto = 'Inocente'
    elif nivel < 3:
        texto = 'Suspeito'
    elif nivel <= 4:
        texto = 'Cúmplice'
    else:
        texto = 'Assassino'
    return texto


def iniciar_interrogatorio():

    recomecar = 1

    while recomecar == 1:
        print('Interrogatório')

        classificacao = 0

        classificacao += obter_resposta("Telefonou para a vítima?\nR: ")
        classificacao += obter_resposta("Esteve no local do crime?\nR: ")
        classificacao += obter_resposta("Mora perto da vítima?\nR: ")
        classificacao += obter_resposta("Devia para a vítima?\nR: ")
        classificacao += obter_resposta("Já trabalhou com a vítima?\nR: ")

        resultado = obter_classificacao(classificacao)

        print('O resultado do interrogatório é: {}'.format(resultado))

        recomecar = obter_resposta('\n\nIniciar um novo interrogatório?\nR: ')

if __name__ == '__main__':
    iniciar_interrogatorio()
