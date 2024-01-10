import unittest
from clas_practise_avto import *


class CarTest(unittest.TestCase):
    def setUp(self):
        make = "GM"
        model = "Malibu"
        self.narhi = 400000
        self.km = 100000
        self.avto1 = Avto(make, model)
        