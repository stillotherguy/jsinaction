__author__ = 'Mitsui'

class bean(object):

    def __init__(self, value):
        self.value = value

    def __cmp__(self, other):
        return self.value - other.value

if __name__ == '__main__':
    print cmp(bean(2), bean(1))

    #unexpect result
    print cmp(1, '2')