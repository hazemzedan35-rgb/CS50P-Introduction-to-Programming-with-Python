import pytest

from fuel import convert

from fuel import gauge

def test_convert_zeroerror():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_greater_value_of_y():
    with pytest.raises(ValueError):
        convert("3/2")
    

def test_negative_input():
    with pytest.raises(ValueError):
        convert("-3/4")
    with pytest.raises(ValueError):
        convert("2/-3")


def test_spaces_input():
    with pytest.raises(ValueError):
        convert("3 / 2")
    with pytest.raises(ValueError):
        convert("3/ 2")


def test_letters_input():
    with pytest.raises(ValueError):
        convert("cat")

    
def test_symbols_input():
    with pytest.raises(ValueError):
        convert("@/4")


def test_whole_ratio():
    assert gauge(1) == "E"
    assert gauge(99) == "F"


def test_middle_conditions():
    assert gauge(50) == "50%"
    assert gauge(6) == "6%"