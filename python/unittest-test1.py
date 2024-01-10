import unittest
from unit1 import *


class Unit1(unittest.TestCase):
    def test_unit1(self):
        test = do(5,6)
        self.assertEqual(test, 11)







unittest.main()