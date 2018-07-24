from unittest import TestCase

from numeros_aleatorios import processa_numeros_aleatorios


class GeraNumerosAleatoriosTests(TestCase):
    
    def test_retorna_quantidade_de_numeros_correta(self):
        numeros = processa_numeros_aleatorios(2)
        self.assertEqual(2, len(numeros))

        numeros = processa_numeros_aleatorios(10)
        self.assertEqual(10, len(numeros))

        numeros = processa_numeros_aleatorios(20)
        self.assertEqual(20, len(numeros))
    
    def test_nao_repete_os_numeros_aleatorios_de_2(self):
        numeros = processa_numeros_aleatorios(2, 1, 2)

        self.assertEqual(2, len(numeros))
        self.assertIn(1, numeros)
        self.assertIn(2, numeros)

    def test_nao_repete_os_numeros_aleatorios_de_10(self):
        numeros = processa_numeros_aleatorios(10, 1, 10)

        self.assertEqual(10, len(numeros))
        self.assertIn(1, numeros)
        self.assertIn(2, numeros)
        self.assertIn(3, numeros)
        self.assertIn(4, numeros)
        self.assertIn(5, numeros)
        self.assertIn(6, numeros)
        self.assertIn(7, numeros)
        self.assertIn(8, numeros)
        self.assertIn(9, numeros)
        self.assertIn(10, numeros)
