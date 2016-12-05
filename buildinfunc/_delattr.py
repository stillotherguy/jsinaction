__author__ = 'Mitsui'

from unittest import TestCase

class Bean(object):

    def __init__(self, name):
        self.name = name

class TestDelAttr(TestCase):

    def testDel(self):
        bean = Bean('Mitsui')

        print bean.name

        delattr(bean, 'name')

        print bean.name
