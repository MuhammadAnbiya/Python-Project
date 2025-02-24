# import pytest

from calculator import squared

def test_positive():
    assert squared(2) == 4
    assert squared(3) == 9

def test_negative():
    assert squared(-2) == 4
    assert squared(-3) == 9

def test_zero():
    assert squared(0) == 0


# def test_str():
#     with pytest.raises(TypeError):
#         squared("cat")

