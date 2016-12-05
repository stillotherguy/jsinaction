__author__ = 'Mitsui'

from unittest import TestCase

class DictTest(TestCase):

    def testDict(self):
        param = dict(name='Ethan', age=28)

        print param

        param = dict([('name', 'Ethan'), ('age', 28)])

        print param

        param = dict([('name', 'Ethan'), ('age', 28)], hobby='basketball')

        print param