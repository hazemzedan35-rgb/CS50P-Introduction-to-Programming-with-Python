from numb3rs import validate

def test_leading_zeros_ip():
    assert validate("1.001.2.4") == False
    assert validate("003.2.4.6") == False

def test_bigger_255_ip():
    assert validate("3.4.5.265") == False
    assert validate("275.1.1.1") == False

def test_maximum_ip():
    assert validate("255.255.255.255") == True

def test_normal_ip():
    assert validate("2.4.6.6") == True
    assert validate("2.5.6.6") == True

def test_wrong_pattern_ip():
    assert validate("2..35.32.4") == False
    assert validate("2.4.4.5.5") == False

def test_non_number_ip():
    assert validate("cat") == False

def test_validate_all_zeros_ip():
    assert validate("0.0.0.0") == True