import unittest
from tests.test_divi import Divi
from tests.test_plain_division import PlainDivide


if __name__ == '__main__':
    unittest.main(verbosity=5)


    # suite = unittest.TestLoader().loadTestsFromNames(PlainDivide, Divi)
    # unittest.TextTestRunner(verbosity=3).run(suite)
    # print(sys.modules[__name__])
    # unittest.main()