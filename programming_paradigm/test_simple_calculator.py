import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Regular case
        self.assertEqual(self.calc.add(-1, 1), 0)  # Adding negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)  # Adding zero
        self.assertEqual(self.calc.add(10, 5), 15)  # Another regular case

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Regular case
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Subtracting zero
        self.assertEqual(self.calc.subtract(10, 15), -5)  # Negative result
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Subtracting larger number

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)  # Regular case
        self.assertEqual(self.calc.multiply(-2, 5), -10)  # Multiplying negative number
        self.assertEqual(self.calc.multiply(0, 10), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Negative multiplied by negative

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # Regular division
        self.assertEqual(self.calc.divide(9, 3), 3)  # Regular division
        self.assertEqual(self.calc.divide(-10, 5), -2)  # Negative divided by positive
        self.assertEqual(self.calc.divide(5, -2), -2.5)  # Positive divided by negative
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero divided by any number
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero should return None

if __name__ == "__main__":
    unittest.main()