from calculator import calculator

def test_add():
    assert calculator.add(3,5) == 8


def test_subtract():
    assert calculator.subtract(3,5) == -2


def test_multiply():
    assert calculator.multiply(3,5) == 15


def test_division():
    assert calculator.division(15, 3) == 5
