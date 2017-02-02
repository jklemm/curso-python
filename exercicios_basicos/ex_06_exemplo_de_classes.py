

class Carro(object):
    def __init__(self):
        print('Materializei um carro!')
        self.nome = 'Carro'

    def __str__(self):
        return self.nome

    def acelerar(self):
        print('VRUMMMMM!!!!!')

    def buzinar(self):
        print('BI BIIIIII!!')


class Fusca(Carro):
    def __init__(self):
        super().__init__()
        self.nome = 'Fuscão 69'

    def __str__(self):
        return self.nome

    def buzinar(self):
        print('FUUUOOWWWWWW!! BARBEIROOOO!!!!')

    def subir_coqueiro(self):
        print('Estou subindo o coqueiro! WOOHOOOO!!!')


if __name__ == '__main__':
    carro = Carro()
    print(carro)
    carro.acelerar()
    carro.acelerar()

    carro2 = Fusca()
    print(carro2)
    carro2.acelerar()
    carro2.buzinar()
    carro2.subir_coqueiro()
