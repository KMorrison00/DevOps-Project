import Butler
import pytest


def test_get():
    butler = Butler.Butler("Jarvis")
    assert butler.get_name() == "Jarvis"


def test_set():
    butler = Butler.Butler("Jarvis")
    butler.set_name("Jenkins")
    assert butler.get_name() == "Jenkins"

