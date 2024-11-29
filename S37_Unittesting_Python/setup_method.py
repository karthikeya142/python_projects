import unittest
import class_method


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = class_method.Calculate()

    def tearDown(self):
        print(" this is teardown method, executes after each test")
        #this actually executes every method after this print statement

    def test_add(self):
        # calculate = class_method.Calculate()
        self.assertEqual(self.calculate.add(2,3),5)
    #testing multiple methods
    def test_sub(self):
        self.assertEqual(self.calculate.sub(10,6),4)
    def test_mul(self):
        self.assertEqual(self.calculate.mul(10,4),40)
    def test_div(self):
            self.assertEqual(self.calculate.div(10,2),5.0)

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
