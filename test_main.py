import unittest
from main import computer_says

class testing_computer_says(unittest.TestCase):
    def test_computer_says(self):
        message = "Hi"
        func = computer_says(message)
        result = " ___\n|[_]|\n|+ ;|  System: \033[47m Hi \033[0m\n`---'\n"
        self.assertEqual(func, result)

if __name__ == "__main__":
    unittest.main()