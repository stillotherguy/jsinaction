__author__ = 'Mitsui'

from unittest import TestCase

class TestComplex(TestCase):

    def testStr(self):
        print complex('1+2j')

    def testNum(self):
        print complex(1)

    def testNumPlus(self):
        print complex(1, 2)
