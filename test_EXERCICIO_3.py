import pytest
import pytest_mock

from EXERCICIO_3 import validar_medida
from EXERCICIO_3 import calcular_preco_volume
from EXERCICIO_3 import ler_dimensoes_objeto
from EXERCICIO_3 import calcular_multiplicador_peso
from EXERCICIO_3 import ler_peso_objeto
from EXERCICIO_3 import calcular_multiplicador_rota
from EXERCICIO_3 import ler_rota
from EXERCICIO_3 import calcular_frete
from EXERCICIO_3 import pedido

class TestPrecoVolume:
    def test_validar_medida(self):
        assert validar_medida(10) == 10
        assert validar_medida(5) == 5

    def test_validar_medida_erro(self):
        assert validar_medida('oito') == -1
        assert validar_medida('dez') == -1


    def test_calcular_preco_volume_menor_1000(self):
        assert calcular_preco_volume(100) == 10
        assert calcular_preco_volume(500) == 10
        assert calcular_preco_volume(999) == 10

    def test_calcular_preco_volume_1000_9999(self):
        assert calcular_preco_volume(1000) == 20
        assert calcular_preco_volume(5001) == 20
        assert calcular_preco_volume(9999) == 20

    def test_calcular_preco_volume_10000_29999(self):
        assert calcular_preco_volume(10000) == 30
        assert calcular_preco_volume(15000) == 30
        assert calcular_preco_volume(29999) == 30

    def test_calcular_preco_volume_30000_100000(self):
        assert calcular_preco_volume(30000) == 20
        assert calcular_preco_volume(50326) == 20
        assert calcular_preco_volume(99999) == 20

    def test_calcular_preco_volume_maior_100000(self):
            assert calcular_preco_volume(100000) == 0
            

    def test_ler_dimensoes_objeto(self,mocker):
        mocker.patch('builtins.input', side_effect = ['10','10','10'])
        assert ler_dimensoes_objeto() == 20

    def test_ler_dimensoes_objeto2(self,mocker):
        mocker.patch('builtins.input', side_effect = ['5','5','5'])
        assert ler_dimensoes_objeto() == 10

    def test_ler_dimensoes_objeto3(self,mocker):
        mocker.patch('builtins.input', side_effect = ['100','100','2'])
        assert ler_dimensoes_objeto() == 30

    def test_ler_dimensoes_objeto4(self,mocker):
        mocker.patch('builtins.input', side_effect = ['100','100','5'])
        assert ler_dimensoes_objeto() == 20

class TestCalculoPeso:
    def test_calcular_multiplicador_peso(self):
        assert calcular_multiplicador_peso(0.01) == 1
        assert calcular_multiplicador_peso(0.5) == 1.5
        assert calcular_multiplicador_peso(5) == 2
        assert calcular_multiplicador_peso(13) == 3

    def test_ler_peso_objeto_1_10(self,mocker):
        mocker.patch('builtins.input', side_effect = ['5'])
        assert ler_peso_objeto() == 2

    def test_ler_peso_objeto_menor_01(self,mocker):
        mocker.patch('builtins.input', side_effect = ['0.05'])
        assert ler_peso_objeto() == 1

    def test_ler_peso_objeto_01_1(self,mocker):
        mocker.patch('builtins.input', side_effect = ['0.3'])
        assert ler_peso_objeto() == 1.5

    def test_ler_peso_objeto_10_30(self,mocker):
        mocker.patch('builtins.input', side_effect = ['15.6'])
        assert ler_peso_objeto() == 3

class TestCalculoRota:
    def test_calcular_multiplicador_rota(self):
        assert calcular_multiplicador_rota('rs') == 1.0
        assert calcular_multiplicador_rota('sr') == 1.0
        assert calcular_multiplicador_rota('bs') == 1.2
        assert calcular_multiplicador_rota('sb') == 1.2
        assert calcular_multiplicador_rota('br') == 1.5
        assert calcular_multiplicador_rota('rb') == 1.5
        # VALOR QUE NAO EXISTE 'SS'
        assert calcular_multiplicador_rota('ss') == 0

    def test_ler_rota_rs(self,mocker):
        mocker.patch('builtins.input', side_effect = ['rs'])
        assert ler_rota() == 1

    def test_ler_rota_sr(self,mocker):
        mocker.patch('builtins.input', side_effect = ['sr'])
        assert ler_rota() == 1

    def test_ler_rota_bs(self,mocker):
        mocker.patch('builtins.input', side_effect = ['bs'])
        assert ler_rota() == 1.2

    def test_ler_rota_sb(self,mocker):
        mocker.patch('builtins.input', side_effect = ['sb'])
        assert ler_rota() == 1.2

    def test_ler_rota_br(self,mocker):
        mocker.patch('builtins.input', side_effect = ['br'])
        assert ler_rota() == 1.5

    def test_ler_rota_rb(self,mocker):
        mocker.patch('builtins.input', side_effect = ['rb'])
        assert ler_rota() == 1.5

class TestCalculoFrete:
    def test_calcular_frete(self):
        assert calcular_frete(10,1.5,9) == 135
        assert calcular_frete(10,10,10) == 1000

class TestPedido:
    def test_pedido_1(self,mocker):
        mocker.patch('builtins.input', side_effect = ['10','10','10','5','rs'])
        assert pedido() == 'Total a Pagar (R$): 40.0 (dimensões: 20.0 * peso: 2.0 * rota: 1.0)'

    def test_pedido_2(self,mocker):
        mocker.patch('builtins.input', side_effect = ['10','10','10','5','sb'])
        assert pedido() == 'Total a Pagar (R$): 48.0 (dimensões: 20.0 * peso: 2.0 * rota: 1.2)'

    def test_pedido_3(self,mocker):
        mocker.patch('builtins.input', side_effect = ['10','10','10','5','rb'])
        assert pedido() == 'Total a Pagar (R$): 60.0 (dimensões: 20.0 * peso: 2.0 * rota: 1.5)'
        


