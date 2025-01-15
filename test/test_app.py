import pytest
from app.app import add, subtract, multiply, divide


def test_add():
    """Тестирует функцию сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    """Тестирует функцию деления."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    # with pytest.raises(ValueError):
    #     divide(5, 0)

def test_subtract():
    assert  subtract(10,5) == 5
    assert subtract(1230, 198) == 1032

def test_multiply():
    assert multiply(10, 2) == 20
    assert multiply(9, 3) == 27
    assert multiply(11, 11) == 121
    assert multiply(1, 3) == 3