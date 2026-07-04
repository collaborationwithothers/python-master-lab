import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_history(self):
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        self.assertEqual(len(self.calc.history), 2)
        self.assertIn("Added 2 to 3 got 5", self.calc.history)
        self.assertIn("Multiplied 4 with 5 got 20", self.calc.history)

if __name__ == '__main__':
    unittest.main()