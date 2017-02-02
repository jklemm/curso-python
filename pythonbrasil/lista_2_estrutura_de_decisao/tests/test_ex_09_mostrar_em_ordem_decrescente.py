from unittest.case import TestCase

from pythonbrasil.lista_2_estrutura_de_decisao.ex_09_mostrar_em_ordem_decrescente \
    import ordenar_em_ordem_decrescente


class OrdenarEmOrdemDecrescenteTests(TestCase):

    def test_todos_numeros_iguais(self):
        self.assertEqual([1, 1, 1], ordenar_em_ordem_decrescente(1, 1, 1))
        self.assertEqual([5, 5, 5], ordenar_em_ordem_decrescente(5, 5, 5))
        self.assertEqual([10, 10, 10], ordenar_em_ordem_decrescente(10, 10, 10))

    def test_dois_numeros_iguais(self):
        self.assertEqual([10, 10, 1], ordenar_em_ordem_decrescente(10, 10, 1))
        self.assertEqual([10, 10, 1], ordenar_em_ordem_decrescente(1, 10, 10))
        self.assertEqual([10, 10, 1], ordenar_em_ordem_decrescente(10, 1, 10))

    def test_primeiro_numero_maior(self):
        self.assertEqual([10, 5, 2], ordenar_em_ordem_decrescente(10, 5, 2))
        self.assertEqual([10, 5, 2], ordenar_em_ordem_decrescente(10, 2, 5))
        self.assertEqual([10, 5, 5], ordenar_em_ordem_decrescente(10, 5, 5))

    def test_segundo_numero_maior(self):
        self.assertEqual([10, 5, 2], ordenar_em_ordem_decrescente(5, 10, 2))
        self.assertEqual([10, 5, 2], ordenar_em_ordem_decrescente(2, 10, 5))
        self.assertEqual([10, 5, 5], ordenar_em_ordem_decrescente(5, 10, 5))

    def test_terceiro_numero_maior(self):
        self.assertEqual([10, 5, 2], ordenar_em_ordem_decrescente(5, 2, 10))
        self.assertEqual([10, 5, 2], ordenar_em_ordem_decrescente(2, 5, 10))
        self.assertEqual([10, 5, 5], ordenar_em_ordem_decrescente(5, 5, 10))
