import Butler
import unittest


class TestButler(unittest.TestCase):

    def test_get(self):
        butler = Butler.Butler("Jarvis")
        self.assertEqual(butler.get_name(), "Jarvis")

    def test_set(self):
        butler = Butler.Butler("Jarvis")
        butler.set_name("Jenkins")
        self.assertEqual(butler.get_name(), "Jenkins")


if __name__ == '__main__':
    unittest.main()