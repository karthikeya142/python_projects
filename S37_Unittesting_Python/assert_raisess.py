import unittest
import class_method


class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calculate = class_method.Calculate()

    def tearDown(self):
        print(" this is teardown method, executes after each test")
        #this actually executes every method after this print statement


    def test_div(self):
            self.assertEqual(self.calculate.div(10,2),5.0)
            with self.assertRaises(ValueError):
                self.calculate.div(10,0)

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
