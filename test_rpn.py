import unittest
import rpn

class TestNoAns(unittest.TestCase): #Needed to isolate this test case
    def test_no_ans(self):
        with self.assertRaises(Exception):
            result = rpn.calculate(":ans 2 +")

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate("1 2 3 +")
    def test_percent(self):
        res = rpn.calculate("72 5% +")
        self.assertEqual(75.6, res)
        res2 = rpn.calculate("72 20% - 5% +")
        self.assertAlmostEqual(60.48, res2) #Different func to avoid floating point error
        res3 = rpn.calculate("20% 10 -")
        self.assertEqual(-8, res3)
    def test_chained(self):
        res = rpn.calculate("6 3 / 5 +")
        self.assertEqual(7, res)
    def test_ans(self):
        rpn.calculate("6 3 +")
        res = rpn.calculate(":ans 2 +")
        self.assertEqual(11, res)
    def test_sum(self):
        res = rpn.calculate("5 3 2 1 10 -2 s")
        self.assertEqual(19, res)

def suite():
    suite = unittest.TestSuite();
    suite.addTest(TestNoAns())
    suite.addTest(TestBasics())
    return suite
    
