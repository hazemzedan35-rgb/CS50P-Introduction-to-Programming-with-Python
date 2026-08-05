import pytest 

from working import check_input

from working import convert

def test_zero_hours():
    with pytest.raises(ValueError):
        check_input("0 AM to 5 PM")
        check_input("9:00 AM to 0 PM")

def test_incorrect_minutes():
    with pytest.raises(ValueError):
        check_input("9:60 AM to 5 PM")
        check_input("9:00 AM to 5:60 PM")

def test_more_12_hour():
    with pytest.raises(ValueError):
        check_input("13 AM to 5 PM")
        check_input("9:00 AM to 14 PM")

def test_normal_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_minutes_in_input():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


