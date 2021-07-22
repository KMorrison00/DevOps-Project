import Butler


def test_get(self):
    butler = Butler.Butler("Jarvis")
    assert butler.get_name() == "Jarvis"


def test_set(self):
    butler = Butler.Butler("Jarvis")
    butler.set_name("Jenkins")
    assert self.butler.get_name() == "Jenkins"

