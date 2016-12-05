__author__ = 'Mitsui'

class valueobj(object):

    def __iter__(self):
        return True

if __name__ == '__main__':
    print any((False,))
    print any((valueobj(), False))