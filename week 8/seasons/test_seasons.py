import pytest

from season import check_valid_input

from season import convert_number_to_letters

def test_correct_date():
    assert check_valid_input("2009-06-22") == (2009, 6, 22)

def test_invalid_date():
    with pytest.raises(SystemExit):
        check_valid_input("2009-6-22")

    with pytest.raises(SystemExit):
        check_valid_input("2009-06-8")

def test_minutes_in_letters():
    assert convert_number_to_letters(525600) == "Five hundred twenty-five thousand, six hundred minutes"