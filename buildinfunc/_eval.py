__author__ = 'Mitsui'


def danger():
    b = -2
    print eval('abs(a - b)')
    print a, b

def safe():
    glo = {'a': 3}
    local = {'b': 4}
    print eval('abs(a - b)', glo, local)
    print glo
    print local

if __name__ == '__main__':
    danger()
    safe()