__author__ = 'Mitsui'

from utils.common_util import tostringarray

if __name__ == '__main__':
    print bytearray()

    print ','.join(tostringarray(bytearray(unicode('U+FFFD'), 'UTF-8')))

    print ','.join(tostringarray(bytearray(5)))

    print ','.join(tostringarray(bytearray([1, 2, 3, 4, 5])))


