# Faça um programa que calcule a quantidade de dinheiro armazenada em uma poupança em vários anos.
# Levando em conta que os juros da poupança anualmente é 12% ao ano (ou 1% ao mês).
# 
# O usuário informa o valor inicial, valor que será adicionado a cada mês, e a quantidade de anos 
# (ou meses pode ser, se você achar mais fácil).
# 
# O programa deverá calcular e informar o valor final que estará na poupança, lembrando que os juros 
# são calculados com o que já está na poupança antes de adicionar o valor mensal.
# 
# Exemplo:
# 
# Informe o valor inicial: 0
# Informe o valor mensal adicionado: 500
# Informe a quantidade de anos: 10
# 
# ....
# 
# Total na poupança: 60.000

JUROS_MENSAL = 1.01


def inicia():
    valor_inicial = float(input('Informe o valor inicial: '))
    valor_mensal = float(input('Informe o valor mensal: '))
    quantidade_anos = int(input('Informe a quantidade de anos: '))

    quantidade_meses = quantidade_anos * 12

    valor_total = valor_inicial
    for mes in range(1, quantidade_meses + 1):  # O + 1 é pro range considerar o último número
        valor_total *= JUROS_MENSAL
        valor_total += valor_mensal

    print('O valor total é de {:.2f} reais'.format(valor_total))

if __name__ == '__main__':
    continuar = True
    while continuar:
        inicia()
        opcao = input('Deseja calcular novamente? S para SIM e N para NÃO')
    
        continuar = opcao.upper() == 'S'
