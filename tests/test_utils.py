from src.utils import saludo, suma, es_par

def test_saludo():
    assert saludo("UIA") == "Hola, UIA!"

def test_suma():
    assert suma(2, 3) == 5

def test_es_par():
    assert es_par(4) is True
    assert es_par(5) is False
