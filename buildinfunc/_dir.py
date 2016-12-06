__author__ = 'Mitsui'

print dir()

import unittest

print(dir(unittest))

class Person(object):

    def Person(self):
        self.name = 'Mitsui'
        self.age = 29

    def info(self):
        return self.name + ' ' + str(self.age)

print(dir(Person()))