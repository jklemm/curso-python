from venda_de_passagens.main import todas_poltronas_estao_vendidas


def test_nao_sao_todas_as_poltronas_vendidas():
    assert todas_poltronas_estao_vendidas(['', '', '']) is not True
    assert todas_poltronas_estao_vendidas(['X', '', '']) is False
    assert todas_poltronas_estao_vendidas(['', 'X', '']) is False
    assert todas_poltronas_estao_vendidas(['', '', 'X']) is False
    assert todas_poltronas_estao_vendidas(['X', 'X', '']) is False
    assert todas_poltronas_estao_vendidas(['', 'X', 'X']) is False
    assert todas_poltronas_estao_vendidas(['X', '', 'X']) is False


def test_todas_as_poltronas_vendidas():
    assert todas_poltronas_estao_vendidas(['X']) is True
    assert todas_poltronas_estao_vendidas(['X', 'X']) is True
    assert todas_poltronas_estao_vendidas(['X', 'X', 'X']) is True
