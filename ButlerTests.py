import unittest
import Butler


class MyTestCase(unittest.TestCase):

    butler = Butler.Butler("Jarvis")

    def test_get(self):
        assert self.butler.get_name() == "Jarvis"

    def test_set(self):
        self.butler.set_name("Jenkins")
        assert self.butler.get_name() == "Jenkins"


if __name__ == '__main__':
    unittest.main()
