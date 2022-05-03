from calculator import Calculator
import unittest
from parameterized import parameterized
from ddt import ddt,data,file_data

class TestAdd(unittest.TestCase):
    """ add()方法测试 """

    def test_add_integer(self):
        """ 整数相加测试 """
        c = Calculator(3, 5)
        self.assertEqual(c.add(), 8)

    def test_add_decimals(self):
        """ 小数相加测试 """
        c = Calculator(3.2, 5.5)
        self.assertEqual(c.add(), 8)

    def test_add_string(self):
        """ 字符串整数相加测试 """
        c = Calculator("7", "9")
        self.assertEqual(c.add(), 16)

    # ……


class TestSub(unittest.TestCase):
    """ sub()方法测试 """

    def test_sub(self):
        c = Calculator(7, 2)
        result = c.sub()
        self.assertEqual(result, 5)


class TestMul(unittest.TestCase):
    """ mul()方法测试 """
    @file_data('mul_data.json')
    def test_mul(self,k1,k2,ans):
        c = Calculator(k1, k2)
        result = c.mul()
        self.assertEqual(result, ans)


class TestDiv(unittest.TestCase):
    """ div()方法测试 """
    @parameterized.expand([
        ("c1",6,2,3),
        ("c2",10,2,5),
        ("c3",8,2,3)
    ])
    def test_div(self,name,k1,k2,ans):
        c = Calculator(k1, k2)
        result = c.div()
        self.assertEqual(result, ans)


if __name__ == '__main__':
    unittest.main()


