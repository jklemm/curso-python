
def obter_salario_atual():
    return float(input('Informe o salário atual: '))


def obter_porcentagem_de_aumento(salario):
    if salario <= 280:
        porcentagem = 0.20
    elif salario <= 700:
        porcentagem = 0.15
    elif salario <= 1500:
        porcentagem = 0.10
    else:
        porcentagem = 0.05
    return porcentagem

if __name__ == '__main__':
    print('Calculadora de salário ajustado')

    salario_atual = obter_salario_atual()
    porcentagem_de_aumento = obter_porcentagem_de_aumento(salario_atual)
    valor_do_aumento = salario_atual * porcentagem_de_aumento
    novo_salario = salario_atual + valor_do_aumento

    print('Salário atual: {:.2f}'.format(salario_atual))
    print('Porcentagem de aumento: {:.0f}%'.format(porcentagem_de_aumento * 100))
    print('Valor do aumento: {:.2f}'.format(valor_do_aumento))
    print('Novo salário ajustado: {:.2f}'.format(novo_salario))
