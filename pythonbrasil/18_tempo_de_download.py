print('Tempo de download\n')

tamanho_do_arquivo = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade_do_link = float(input('Informe a velocidade do link (em Mbps): '))

tempo_aproximado_em_segundos = tamanho_do_arquivo / velocidade_do_link

tempo_aproximado_em_minutos = tempo_aproximado_em_segundos / 60

print('Tempo aproximado de download: {:.2f} minutos'.format(tempo_aproximado_em_minutos))
