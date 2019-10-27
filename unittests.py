import unittest

from kata_app import addition
from kata_app import difference
from kata_app import division
from kata_app import multiply
from kata_app import modulas


class AdditionTest(unittest.TestCase):
    def test_addition_int(self):
        # Test Constructor Addition Method.
        data = [12, 4, 53, 34, 7]
        result = addition(data)
        self.assertEqual(result, 110)

class DifferenceTest(unittest.TestCase):
    def test_difference_int(self):
        # Test Constructor Difference Method.
        result = difference(123, 54)
        self.assertEqual(result, 69)

class DivisionTest(unittest.TestCase):
    def test_division_int(self):
        # Test Constructor Division Method.
        result = division(120, 6)
        self.assertEqual(result, 20)    

class MultiplyTest(unittest.TestCase):
    def test_multiply_int(self):
        # Test Constructor Multiply Method.
        result = multiply(15, 4)
        self.assertEqual(result, 60)              

class ModulasTest(unittest.TestCase):
    def test_modulas_int(self):
        # Test Constructor Modulas Method.
        result = modulas(5, 2)
        self.assertEqual(result, 1)        

if __name__ == '__main__':
    unittest.main()



