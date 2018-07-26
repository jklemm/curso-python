from unittest import TestCase

from agrupa_numeros.agrupa import agrupa


class AgrupaTests(TestCase):
    
    def test_retorna_vazio(self):
        retorno = agrupa('')
        self.assertEqual('', retorno)

    def test_retorno_de_um_unico_numero(self):
        retorno = agrupa('10')
        self.assertEqual('[10]', retorno)
       
    def test_retorno_de_dois_numeros(self):
        retorno = agrupa('1, 2')
        self.assertEqual('[1-2]',retorno)
