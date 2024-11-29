import unittest
import class_method
calculate =class_method.Calculate()

class TestCalculate(unittest.TestCase):

    def test_add(self):
        # calculate = class_method.Calculate()
        self.assertEqual(calculate.add(2,3),5)
    #testing multiple methods
    def test_sub(self):
        self.assertEqual(calculate.sub(10,6),4)
    def test_mul(self):
        self.assertEqual(calculate.mul(10,4),40)
    def test_div(self):
            self.assertEqual(calculate.div(10,2),5.0)

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
