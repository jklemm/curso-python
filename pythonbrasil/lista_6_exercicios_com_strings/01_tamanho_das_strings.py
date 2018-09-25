# Tamanho de strings.
# Faça um programa que leia 2 strings e informe o 
# conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo 
# comprimento e são iguais ou diferentes no conteúdo.       

if __name__ == '__main__':
    
    mensagem_1 = input('Digite uma frase: ').strip()
    mensagem_2 = input('Digite outra frase: ').strip()

    comprimento_mensagem_1 = len(mensagem_1)
    comprimento_mensagem_2 = len(mensagem_2)
    
    print('{}: {} caracteres'.format(mensagem_1, comprimento_mensagem_1))
    print('{}: {} caracteres'.format(mensagem_2, comprimento_mensagem_2))

    possuem_o_mesmo_comprimento = comprimento_mensagem_1 == comprimento_mensagem_2
    if possuem_o_mesmo_comprimento:
        print('As duas mensagens possuem o mesmo comprimento!')
    else:
        print('As duas mensagens NÃO possuem o mesmo comprimento!')

    if possuem_o_mesmo_comprimento and mensagem_1 == mensagem_2:
        print('As duas mensagens são iguais!')
    else:
        print('As duas mensagens são diferentes!')

