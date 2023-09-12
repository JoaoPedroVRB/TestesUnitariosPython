import pytest

from EXERCICIO_1 import desconto

def test_desconto_10_99():
    resultado = desconto(10, 30)
    assert resultado == (285.0, 300.0)

def test_desconto_100_999():
    resultado = desconto(10,200)
    assert resultado == (1800,2000)

def test_desconto_acima_de_1000():
    resultado = desconto(10,12000)
    assert resultado == (102000,120000)

def test_sem_desconto_1_9():
    resultado = desconto(10,5)
    assert resultado == (50,50)

