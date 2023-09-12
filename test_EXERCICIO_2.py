import pytest
import pytest_mock

from EXERCICIO_2 import cardapio
from EXERCICIO_2 import pedido

class TestPedido:
    def test_pedido(self):
        assert pedido(100) == 9
        assert pedido(105) == 17
        assert pedido(101) == 11
        assert pedido(102) == 12
        assert pedido(103) == 12
        assert pedido(104) == 14
        assert pedido(200) == 5
        assert pedido(201) == 4

    def test_pedido_erro(self):
        resultado = pedido(300)
        assert resultado == 0

class TestCardapio:
    def test_cardapio(self,mocker):
        mocker.patch('builtins.input', side_effect = ['100', '1', '101', '2'])
        total = cardapio()
        assert total == 20.00

    def test_cardapio_com_erro(self,mocker):
        mocker.patch('builtins.input', side_effect = ['100', '1', '300', '1', '101','2'])
        total = cardapio()
        assert total == 20.00

    def test_cardapio_pedindo_todos(self,mocker):
        mocker.patch('builtins.input', side_effect = ['100', '1', '101', '1', '102','1','103','1','104','1','105','1','200','1','201','2'])
        assert cardapio() == 84 