def calcula_salario(quantidade_horas, valor_hora):
    return quantidade_horas * valor_hora

def pedir_float(mensagem):
    return float(input(mensagem))

def sistema():
    print('Calcula o salário mensal')

    valor = pedir_float('Informe quanto você ganha por hora: R$ ')
    quantidade = pedir_float('Informe o número de horas trabalhadas no mês: ')

    salario = calcula_salario(quantidade, valor)

    print('O total do salário neste mês foi R$ {:.2f}'.format(salario))

if __name__ == '__main__':
    sistema()
