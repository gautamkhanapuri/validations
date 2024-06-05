import unittest
from source.division_script import plain_divide
# import sys
# from test_divi import Divi


class PlainDivide(unittest.TestCase):

    def test_plain_divide_positive_numbers(self):
        assert plain_divide(10, 2, 3) == (5.0, 0), "Expected result = 5.0 and remainder = 0"
        assert plain_divide(10, 3, 3) == (3.333, 1), "Expected result = 3.333 and remainder = 1"
        assert plain_divide(0, 3, 3) == (0.0, 0), "Expected result = 0.0 and remainder = 0"
        assert plain_divide(1222, 9934, 2) == (0.12, 2992), "Expected result = 0.12 and remainder = 2992"
        assert plain_divide(1222, 9934, 10) == (0.1230118783, 9678), "Expected result = 0.1230118783 and remainder = 9678"
        assert plain_divide(17, 9, 10) == (1.8888888888, 8), "Expected result = 1.8888888888 and remainder = 8"
        assert plain_divide(14, 99, 10) == (0.1414141414, 14), "Expected result = 0.1414141414 and remainder = 14"

    def test_plain_divide_negative_numbers(self):
        assert plain_divide(-10, 2, 3) == (-5.0, 0), "Expected result = -5.0 and remainder = 0"
        assert plain_divide(10, -2, 3) == (-5.0, 0), "Expected result = -5.0 and remainder = 0"
        assert plain_divide(-10, 3, 3) == (-3.333, 1), "Expected result = 3.333 and remainder = 1"
        assert plain_divide(0, -3, 3) == (0.0, 0), "Expected result = 0.0 and remainder = 0"
        assert plain_divide(-33, -8, 3) == (4.125, 0), "Expected result = 4.125 and remainder = 0"
        assert plain_divide(-33, -8, 2) == (4.12, 4), "Expected result = 4.12 and remainder = 4"

    def test_plain_divide_digits_parameter_errors(self):
        assert plain_divide(10, 3, 20) == (3.333333333333333, 1), "Expected result = 3.333333333333333 and remainder = 1"
        assert plain_divide(22, 7, 20) == (3.142857142857142, 6), "Expected result = 3.142857142857142 and remainder = 6"
        assert plain_divide(22, 7, -20) == (3.142857142857142, 6), "Expected result = 3.142857142857142 and remainder = 6"
        assert plain_divide(10, 3, -3) == (3.333, 1), "Expected result = 3.333 and remainder = 1"
        assert plain_divide(-10, 2, -3) == (-5.0, 0), "Expected result = -5.0 and remainder = 0"
        assert plain_divide(0, 3, 3.3) == (0.0, 0), "Expected result = 0.0 and remainder = 0"
        assert plain_divide(-10, 3, 3.8) == (-3.333, 1), "Expected result = 3.333 and remainder = 1"

    def test_divisio_by_zero(self):
        try:
            assert plain_divide(-10, 0, -3) == "Cannot divide by zero.", "Expected ZeroDivisionError"
        except ZeroDivisionError:
            print("Cannot divide by 0.")


# to run this test file alone
# if __name__ == '__main__':
#     unittest.main(verbosity=5)

    # suite = unittest.TestLoader().loadTestsFromNames(PlainDivide, Divi)
    # unittest.TextTestRunner(verbosity=4).run(suite)
    # print(sys.modules[__name__])
    # unittest.main()
