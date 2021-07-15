import unittest
import Butler

class MyTestCase(unittest.TestCase):

    butler = Butler.Butler()

    def test_get(self):
        self.assertEqual(self.butler.get_name(), "Jarvis")

    def test_set(self):
        self.butler.set_name("Jenkins")
        self.assertEqual(self.butler.get_name(), "Jenkins")

if __name__ == '__main__':
    unittest.main()
