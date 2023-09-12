import pytest

@pytest.fixture
def pecas():
    return [
        {
            'codigo': 1,
            'nome': 'peca1',
            'fabricante': 'fabricante1',
            'valor': 20.60
        },
        {
            'codigo': 2,
            'nome': 'peca2',
            'fabricante': 'fabricante1',
            'valor': 50.20
        }
    ]