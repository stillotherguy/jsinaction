__author__ = 'Mitsui'

class valueobj(object):

    def __index__(self):
        return 1;

if __name__ == '__main__':
    print bin(valueobj())