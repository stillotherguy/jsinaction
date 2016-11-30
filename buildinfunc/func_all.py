__author__ = 'Mitsui'

class valueobj(object):

    def __iter__(self):
        return True

if __name__ == '__main__':
    print all((valueobj(), valueobj()))
    print all((valueobj(), valueobj(), False))