import unittest
from source.division_script import divi


class Divi(unittest.TestCase):

    def test_divi_equal_dividend_and_divisor(self):
        # when x and y are equal
        # fr = True and fr = False
        assert divi(2, 2, False) == (1, 0), "expecting q = 1 and x = 0"
        assert divi(2, 2, True) == (1, 0), "expecting q = 1 and x = 0"

    def test_divi_dividend_lessthan_divisor_frFalse(self):
        # when fr = False
        # abs(x) < abs(y)
        # x % y != 0
        assert divi(1, 2, False) == (0, 1), "expecting q = 0 and x = 1"
        assert divi(1, -2, False) == (0, 1), "expecting q = 0 and x = 1"
        assert divi(-1, 2, False) == (0, -1), "expecting q = 0 and x = -1"
        assert divi(-1, -2, False) == (0, -1), "expecting q = 0 and x = -1"

    def test_divi_dividend_greaterthan_divisorfrFalse(self):
        # when fr = False
        # abs(x) > abs(y)
        # x % y == 0
        assert divi(10, 2, False) == (5, 0), "expecting q = 5 and x = 0"
        assert divi(-10, 2, False) == (-5, 0), "expecting q = -5 and x = 0"
        assert divi(10, -2, False) == (-5, 0), "expecting q = -5 and x = 0"
        assert divi(-10, -2, False) == (5, 0), "expecting q = 5 and x = 0"
        assert divi(-8, -2, False) == (4, 0), "expecting q = 4 & x = 0"

    def test_divi_dividend_greaterthan_divisor_and_x_notdivisibleby_yfrFalse(self):
        # when fr = False
        # abs(x) > abs(y)
        # x % y != 0
        assert divi(11, 2, False) == (5, 1), "expecting q = 5 and x = 1"
        assert divi(-11, 2, False) == (-5, -1), "expecting q = -5 and x = -1"
        assert divi(11, -2, False) == (-5, 1), "expecting q = -5 and x = 1"
        assert divi(-11, -2, False) == (5, -1), "expecting q = 5 and x = -1"

    def test_divi_dividend_lessthan_divisor_frTrue(self):
        # when fr = True
        # abs(x) < abs(y)
        # x*10 % y == 0
        assert divi(1, 2, True) == (5, 0), "expecting q = 0 and x = 1"
        assert divi(1, -2, True) == (-5, 0), "expecting q = 0 and x = 1"
        assert divi(-1, 2, True) == (-5, 0), "expecting q = 0 and x = -1"
        assert divi(-1, -2, True) == (5, 0), "expecting q = 0 and x = -1"

    def test_divi_dividend_lessthan_divisor_and_x_notdivisibleby_yfrTrue(self):
        # abs(x) < abs(y)
        # x*10 % y != 0
        assert divi(1, 3, True) == (3, 1), "expecting q = 3 and x = 1"
        assert divi(1, -3, True) == (-3, 1), "expecting q = -3 and x = 1"
        assert divi(-1, 3, True) == (-3, -1), "expecting q = -3 and x = -1"
        assert divi(-1, -3, True) == (3, -1), "expecting q = 3 and x = -1"

    def test_divi_dividend_greaterthan_divisorfrTrue(self):
        # when fr = True
        # abs(x) > abs(y)
        # x % y == 0
        assert divi(10, 2, True) == (5, 0), "expecting q = 5 and x = 0"
        assert divi(-10, 2, True) == (-5, 0), "expecting q = -5 and x = 0"
        assert divi(10, -2, True) == (-5, 0), "expecting q = -5 and x = 0"
        assert divi(-10, -2, True) == (5, 0), "expecting q = 5 and x = 0"

    def test_divi_dividend_greaterthan_divisor_and_x_notdivisibleby_yfrTrue(self):
        # when fr = True
        # abs(x) > abs(y)
        # x % y != 0
        assert divi(11, 2, True) == (5, 1), "expecting q = 5 and x = 1"
        assert divi(-11, 2, True) == (-5, -1), "expecting q = -5 and x = -1"
        assert divi(11, -2, True) == (-5, 1), "expecting q = -5 and x = 1"
        assert divi(-11, -2, True) == (5, -1), "expecting q = 5 and x = -1"

    def test_divi_dividend_equalto_zero(self):
        # x = 0
        assert divi(0, 2, False) == (0, 0), "expecting q = 0 and x = 0"
        assert divi(0, 2, True) == (0, 0), "expecting q = 0 and x = 0"

    def test_divisorzero(self):
        try:
            assert divi(2, 0, False) == "Cannot divide by 0.", "expecting ZeroDivisionError"
            assert divi(2, 0, True) == "Cannot divide by 0.", "expecting ZeroDivisionError"
        except ZeroDivisionError:
            print("Cannot divide by 0.")





# to run this test file alone
# if __name__ == '__main__':
#      unittest.main(verbosity=5)