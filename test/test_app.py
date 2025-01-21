import pytest
from app.app import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 15, 25),
    (26, 4, 30),
    (1, 0, 1)
])

def test_add(a,b,expected):
    assert a + b == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (2, 3, -1),
    (15, 10, 5),
    (26, 4, 22),
    (1, 0, 1)
])

def test_subtract(a,b,expected):
    assert a - b == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (2, 3, 6),
    (15, 10, 150),
    (26, 4, 104),
    (1, 0, 0)
])
def test_multiply(a, b, expected):
    assert a * b == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 0.5),
    (4, 2, 2),
    (15, 10, 1.5),
    (26, 4, 6.5),
    (1, 0, ValueError)
])
def test_divide(a, b, expected):
    if b == 0:
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            raise ValueError("Деление на ноль невозможно")
    else:
        assert a / b == expected




