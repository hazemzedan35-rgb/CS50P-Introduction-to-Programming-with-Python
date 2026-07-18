import pytest

from plates import is_valid

def test_first2_letters():
    assert is_valid("mm100") == True
    assert is_valid("MM200") == True
    assert is_valid("2m989") == False
    assert is_valid("m1854") == False

def test_first_number():
    assert is_valid("mm023") == False
    assert is_valid("mm102") == True

def test_number_location():
    assert is_valid("mm345") == True
    assert is_valid("mm10a") == False


def test_plate_size():
    assert is_valid("m") == False
    assert is_valid("mn876") == True
    assert is_valid("mmn1245") == False


def test_presence_of_symbols():
    assert is_valid("mm#23") == False
    assert is_valid("mm234") == True


def test_spaces():
    assert is_valid("  mm234") == False
    assert is_valid("mn123 ") == False
    assert is_valid("mm 234") == False


def test_empty_input():
    assert is_valid("") == False