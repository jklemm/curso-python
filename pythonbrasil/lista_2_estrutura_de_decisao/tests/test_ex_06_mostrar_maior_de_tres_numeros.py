from unittest.case import TestCase

from pythonbrasil.lista_2_estrutura_de_decisao.ex_06_mostrar_maior_de_tres_numeros import obter_maior_numero


class ObterMaiorNumeroTests(TestCase):

    def test_todos_numeros_iguais(self):
        self.assertEqual(1, obter_maior_numero(1, 1, 1))
        self.assertEqual(5, obter_maior_numero(5, 5, 5))
        self.assertEqual(10, obter_maior_numero(10, 10, 10))

    def test_dois_numeros_iguais(self):
        self.assertEqual(10, obter_maior_numero(10, 10, 1))
        self.assertEqual(10, obter_maior_numero(1, 10, 10))
        self.assertEqual(10, obter_maior_numero(10, 1, 10))

    def test_primeiro_numero_maior(self):
        self.assertEqual(10, obter_maior_numero(10, 5, 2))
        self.assertEqual(10, obter_maior_numero(10, 2, 5))
        self.assertEqual(10, obter_maior_numero(10, 5, 5))

    def test_segundo_numero_maior(self):
        self.assertEqual(10, obter_maior_numero(5, 10, 2))
        self.assertEqual(10, obter_maior_numero(2, 10, 5))
        self.assertEqual(10, obter_maior_numero(5, 10, 5))

    def test_terceiro_numero_maior(self):
        self.assertEqual(10, obter_maior_numero(5, 2, 10))
        self.assertEqual(10, obter_maior_numero(2, 5, 10))
        self.assertEqual(10, obter_maior_numero(5, 5, 10))
