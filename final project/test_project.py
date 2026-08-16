import pytest

from project import check_temprature, check_humidity, check_hive_status

def test_normal_temprature():
    assert check_temprature(34.5) == True
    assert check_temprature(36.0) == True


def test_abnormal_temprature():
    assert check_temprature(37.4) == False
    assert check_temprature(32.5) == False


def test_normal_humidity():
    assert check_humidity(50.0) == True
    assert check_humidity(60.0) == True


def test_abnormal_humidity():
    assert check_humidity(40.5) == False
    assert check_humidity(80.3) == False


def test_out_put():
    assert check_hive_status(True, True) == "Status: Optimal (Hive is healthy)."
    assert check_hive_status(True, False) == "Status: warning humidity in hive isn't in the normal state."
    assert check_hive_status(False, True) == "Status: warning temprature in hive isn't in the normal state."
    assert check_hive_status(False, False) == "Status: Both temprature and humidity aren't in normal state "