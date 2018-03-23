SEGUNDOS_EM_UM_DIA = 86400
SEGUNDOS_EM_UMA_HORA = 3600
SEGUNDOS_EM_UM_MINUTO = 60

dias = float(input('Digite a quantidade de dias: '))
horas = float(input('Digite a quantidade de horas: '))
minutos = float(input('Digite a quantidade de minutos: '))
segundos = float(input('Digite a quantidade de segundos: '))

dias_em_segundos = dias * SEGUNDOS_EM_UM_DIA
horas_em_segundos = horas * SEGUNDOS_EM_UMA_HORA
minutos_em_segundos = minutos * SEGUNDOS_EM_UM_MINUTO

total_em_segundos = dias_em_segundos + horas_em_segundos + minutos_em_segundos + segundos

print('O Total é {} segundos'.format(total_em_segundos))
