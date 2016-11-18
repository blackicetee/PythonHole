import unittest


# Class implements the functions of a calculus
class Calculus:

    __results = []

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def div(x, y):
        if y != 0:
            return x / y
        else:
            # division by 0
            return "division by zero is not defined"

    @staticmethod
    def mul(x, y):
        return x * y

    @staticmethod
    def mod(x, y):
        return x % y


# TestClass of Calculus
class TestCalculus(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculus().add(12, 98), 110)

    def test_sub(self):
        self.assertEqual(Calculus().sub(44, 88), -44)
        self.assertEqual(Calculus().sub(99, 33), 66)

    def test_div(self):
        self.assertEqual(Calculus.div(1, 0), "division by zero is not defined")
        self.assertEqual(Calculus.div(30, 10), 3)
        self.assertEqual(Calculus.div(5, 2), 2.5)

    def test_mul(self):
        self.assertEqual(Calculus.mul(10, 66), 660)
        self.assertEqual(Calculus.mul(0.5, 100), 50)

    def test_mod(self):
        self.assertEqual(Calculus.mod(9, 2), 1)



