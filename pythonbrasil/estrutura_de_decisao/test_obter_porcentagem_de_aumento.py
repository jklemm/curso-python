from unittest.case import TestCase

from .ex_11_organizacoes_tabajara import obter_porcentagem_de_aumento


class ObterPorcentagemDeAumentoTests(TestCase):

    def test_salario_igual_ou_abaixo_de_280(self):
        porcentagem = obter_porcentagem_de_aumento(200)
        self.assertEqual(porcentagem, 0.20)

        porcentagem = obter_porcentagem_de_aumento(280)
        self.assertEqual(porcentagem, 0.20)

    def test_salario_igual_ou_abaixo_de_700(self):
        porcentagem = obter_porcentagem_de_aumento(500)
        self.assertEqual(porcentagem, 0.15)

        porcentagem = obter_porcentagem_de_aumento(700)
        self.assertEqual(porcentagem, 0.15)
