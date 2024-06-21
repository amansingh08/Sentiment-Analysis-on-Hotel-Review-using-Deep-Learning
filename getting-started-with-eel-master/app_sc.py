import unittest


class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        a = 5
        b = 10
        result = a + b
        self.assertEqual(result, 15, "Addition failed")

    def test_subtraction(self):
        a = 10
        b = 5
        result = a - b
        self.assertEqual(result, 5, "Subtraction failed")

    def test_multiplication(self):
        a = 5
        b = 10
        result = a * b
        self.assertEqual(result, 50, "Multiplication failed")

    def test_division(self):
        a = 10
        b = 5
        result = a / b
        self.assertEqual(result, 2, "Division failed")


if __name__ == '__main__':
    unittest.main()
