from unittest import TestCase

from testes_unitarios.arquivo import soma, potenciacao, subtracao, todas_as_poltronas_estao_vendidas


class TesteCoisasDeMatematica(TestCase):
    
    def test_soma_basica_de_dois_numeros_positivos(self):
        self.assertEqual(0, soma(0, 0))
        self.assertEqual(2, soma(1, 1))
        self.assertEqual(4, soma(2, 2))

    def test_soma_basica_de_dois_numeros_negativos(self):
        self.assertEqual(-2, soma(-1, -1))
        self.assertEqual(-4, soma(-2, -2))

    def test_potenciacao(self):
        self.assertEqual(4, potenciacao(2, 2))
        self.assertEqual(1, potenciacao(1, 1))
        self.assertEqual(1, potenciacao(1, 0))

    def test_potenciacao_potencia_um(self):
        self.assertEqual(1, potenciacao(1, 1))
        self.assertEqual(5, potenciacao(5, 1))

    def test_subtracao(self):
        self.assertEqual(3, subtracao(5, 2))
        self.assertEqual(0, subtracao(1, 1))


class TesteCoisasDePassagemDeOnibus(TestCase):

    def test_retorna_falso_quando_nenhuma_poltrona_vendida(self):
        poltronas = ['', '', '']

        resultado = todas_as_poltronas_estao_vendidas(poltronas)
        
        self.assertFalse(resultado)

    def test_retorna_falso_quando_apenas_uma_poltrona_vendida(self):
        poltronas = ['', '', 'X']

        resultado = todas_as_poltronas_estao_vendidas(poltronas)
        
        self.assertFalse(resultado)

    def test_retorna_falso_quando_duas_poltronas_vendidas(self):
        poltronas = ['X', '', 'X']

        resultado = todas_as_poltronas_estao_vendidas(poltronas)
        
        self.assertFalse(resultado)

    def test_retorna_true_quando_todas_poltronas_vendidas(self):
        poltronas = ['X', 'X', 'X']

        resultado = todas_as_poltronas_estao_vendidas(poltronas)
        
        self.assertTrue(resultado)

    def test_retorna_true_quando_tem_poltrona_Y(self):
        poltronas = ['', '', 'Y']

        resultado = todas_as_poltronas_estao_vendidas(poltronas)
        
        self.assertTrue(resultado)

    def test_retorna_true_quando_tem_varias_x_e_uma__Y(self):
        poltronas = ['X', 'X', 'Y']

        resultado = todas_as_poltronas_estao_vendidas(poltronas)
        
        self.assertTrue(resultado)
