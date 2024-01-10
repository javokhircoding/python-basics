import unittest
from unit import get_full_name


class TestName(unittest.TestCase):
    def test_ism(self):
        test = get_full_name('javohir', 'shermatov')
        self.assertEqual(test, 'Javohir Shermatov')



    def test_otasi_ism(self):
        test = get_full_name('javohir', 'shermatov', 'yigitaliyevich')
        self.assertEqual(test, 'Javohir Yigitaliyevich Shermatov')



unittest.main()