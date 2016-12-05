__author__ = 'Mitsui'

from unittest import TestCase

class complieTest(TestCase):

    def testEval(self):
        result = compile('3*x + 4*y', '', mode='eval')
        print type(result)
        print eval(result, dict(x=1, y=2))

    def testExec(self):
        result = compile('print n if n>0 else -n', '', mode='exec')
        print(type(result))
        exec(result, dict(n=1))

