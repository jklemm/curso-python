from unittest.case import TestCase

from exercicios_basicos.ex_01_calculadora_soma import efetua_soma


class TestSoma(TestCase):

    def test_soma_esta_correta(self):
        self.assertEqual(0, efetua_soma())

    def test_soma_esta_correta_quando_tem_negativos(self):
        self.assertEqual(10, efetua_soma(-1, 1, 10))
