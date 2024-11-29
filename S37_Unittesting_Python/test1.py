import  unittest
import first_test

class TestDemo(unittest.TestCase):

    def test_add(self):
        self.assertEqual(first_test.add(2,2),4)
        #to checking multiple asserts
    def test_sub(self):
        self.assertEqual(first_test.sub(10,4),6)
    def test_mul(self):
        self.assertEqual(first_test.mul(10,4),40)
    def test_div(self):
            self.assertEqual(first_test.div(10,2),5.0)



if __name__ =='__main__':
    unittest.main()