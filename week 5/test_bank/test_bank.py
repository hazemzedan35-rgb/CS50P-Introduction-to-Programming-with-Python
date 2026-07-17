import pytest

from bank import value

def test_hello_lowercase():
    assert value("hello") == "$0"
    assert value("hello, mohamed") == "$0"


def test_hello_uppercase():
    assert value("Hello") == "$0"
    assert value("HELLO, MOHAMED") == "$0"


def test_h_lowercase():
    assert value("hi, everybody") == "$20"
    assert value("hey man") == "$20"


def test_any_letter_else():
    assert value("good morning") == "$100"
    assert value("whats up") == "$100"


def test_empty_input():
    assert value("") == "$100"
