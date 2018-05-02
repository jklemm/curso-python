
class Casa(object):

    # A função __init__ é sempre invocada quando você cria um objeto da classe, neste caso, Casa()
    def __init__(self):
        self.cor = 'vermelha'

    def abrir_porta(self):
        print('Abriu a porta!')


class CasaDoLoboMau(Casa):
    def __init__(self):
        # Nessa linha abaixo, a CasaDoLoboMau tem que chamar o init da classe Pai: Casa
        super(CasaDoLoboMau, self).__init__()
        self.cor = 'envelhecida'

    def abrir_porta(self):
        print('Abriu a porta! NHAC, Lobo mau te pegou!')


if __name__ == '__main__':
    casinha = Casa()
    casinha.abrir_porta()
    
    casa_do_lobo_mau = CasaDoLoboMau()
    casa_do_lobo_mau.abrir_porta()
    
    print('fim!')
