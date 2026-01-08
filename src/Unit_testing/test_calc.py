import unittest
import Calc

class TestCalc(unittest.TestCase):

    def test_add(self):

        self.assertEqual(Calc.add(10,5),15)
        self.assertEqual(Calc.add(-1,1),0)
        self.assertEqual(Calc.add(-1,-1),-2)


    def test_subtract(self):

        self.assertEqual(Calc.subtract(10,5),5)
        self.assertEqual(Calc.subtract(1,1),0)
        self.assertEqual(Calc.subtract(10,-5),15)

    def test_multiply(self):

        self.assertEqual(Calc.multiply(10,5),50)

    def test_divide(self):
        self.assertEqual(Calc.divide(10,5),2)

if __name__ == '__main__':
    unittest.main()
