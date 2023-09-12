import pytest 
import pytest_mock

from EXERCICIO_4 import gerar_codigo
from EXERCICIO_4 import cadastrar_peca
from EXERCICIO_4 import imprimir_peca
from EXERCICIO_4 import consultar_pecas 
from EXERCICIO_4 import remover_peca

class TestCadastroPeca:
    def test_gerar_codigo(self,pecas):
        assert gerar_codigo([]) == 1
        assert gerar_codigo(pecas) == 3

    def test_cadastrar_peca(self,pecas,mocker):
        mocker.patch('builtins.input', side_effect = ['peca3', 'fabricante3', '30.6'])
        assert cadastrar_peca(pecas) == 3

class TestConsultaPeca:
    def test_imprimir_peca(self,pecas):
        assert imprimir_peca(pecas[0]) == '001 fabricante1 20.60'
        assert imprimir_peca(pecas[1]) == '002 fabricante1 50.20'

    def test_consultar_pecas_op_1(self,pecas,mocker):
        mocker.patch('builtins.input', side_effect = ['1','4'])
        assert consultar_pecas(pecas) == 2

    def test_consultar_pecas_op_2(self,pecas,mocker):
        mocker.patch('builtins.input', side_effect = ['2','1','4'])
        assert consultar_pecas(pecas) == 1

    def test_consultar_pecas_op_3(self,pecas,mocker):
        mocker.patch('builtins.input', side_effect = ['3','fabricante1','4'])
        assert consultar_pecas(pecas) == 2

    def test_consultar_pecas_op_erro(self,pecas,mocker):
        mocker.patch('builtins.input', side_effect = ['5'])
        assert consultar_pecas(pecas) == -1

class TestRemovePeca:
    def test_remover_peca(self,pecas,mocker):
        mocker.patch('builtins.input', side_effect = ['1'])
        assert remover_peca(pecas) == 1

    def test_remover_peca_codigo_invalido(self,pecas,mocker):
        mocker.patch('builtins.input', side_effect = ['50'])
        assert remover_peca(pecas) == 2

