import pytest
from divide_function import divide

def test_divide_valid_numbers():
    assert divide(10, 2) == 5.0

def test_divide_with_zero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        divide(8, 0)

def test_divide_with_string_in_denominator():
    with pytest.raises(TypeError):
        divide(20, "Jose")

def test_divide_with_string_in_numerator():
    with pytest.raises(TypeError):
        divide("Jose", 5)
