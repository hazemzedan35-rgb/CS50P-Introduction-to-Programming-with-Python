# python -m pytest" the file location "

import pytest

from twttr import shorten

def test_shorten_lowerCase():
    assert shorten("moamen") == "mmn"
    assert shorten("main") == "mn"


def test_shorten_upperCase():
    assert shorten("MOAMEN") == "MMN"
    assert shorten("MAIN") == "MN"


def test_shorten_Symbols():
    assert shorten("#$$%%%^^&*()_+#%@$%%!@$@#") == "#$$%%%^^&*()_+#%@$%%!@$@#"
    assert shorten("+_()(&^?<<{~@$#~~$#@!})") == "+_()(&^?<<{~@$#~~$#@!})"


def  test_shorten_empty():
    assert shorten("") == ""


def test_shorten_empty_input():
    assert shorten("") == ""
