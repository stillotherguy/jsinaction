__author__ = 'Mitsui'

class valueobj(object):
    def __call__(self, *args, **kwargs):
        pass

class valueobj1(object):
        pass

if __name__ == '__main__':
    print callable(valueobj())
    print callable(valueobj)

    print callable(valueobj1())
    print callable(valueobj1)