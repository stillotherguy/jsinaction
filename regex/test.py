__author__ = 'Mitsui'

import re
from re import compile

if __name__ == '__main__':
    regex = compile('(?=abc)(?P<value>.+)(?=efg)', re.IGNORECASE)
    print regex.match('abcdefg').groupdict()