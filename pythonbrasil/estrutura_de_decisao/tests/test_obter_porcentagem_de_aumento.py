from unittest.case import TestCase

from pythonbrasil.estrutura_de_decisao.ex_11_organizacoes_tabajara import obter_porcentagem_de_aumento


class ObterPorcentagemDeAumentoTests(TestCase):

    def test_salario_igual_ou_abaixo_de_280(self):
        porcentagem = obter_porcentagem_de_aumento(200)
        self.assertEqual(porcentagem, 20)

        porcentagem = obter_porcentagem_de_aumento(280)
        self.assertEqual(porcentagem, 20)

    def test_salario_igual_ou_abaixo_de_700(self):
        porcentagem = obter_porcentagem_de_aumento(500)
        self.assertEqual(porcentagem, 15)

        porcentagem = obter_porcentagem_de_aumento(700)
        self.assertEqual(porcentagem, 15)

    def test_salario_igual_ou_abaixo_de_1500(self):
        porcentagem = obter_porcentagem_de_aumento(1000)
        self.assertEqual(porcentagem, 10)

        porcentagem = obter_porcentagem_de_aumento(1500)
        self.assertEqual(porcentagem, 10)

    def test_salario_maior_que_1500(self):
        porcentagem = obter_porcentagem_de_aumento(1501)
        self.assertEqual(porcentagem, 5)

        porcentagem = obter_porcentagem_de_aumento(30000)
        self.assertEqual(porcentagem, 5)
