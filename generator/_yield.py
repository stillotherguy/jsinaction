__author__ = 'Mitsui'

def gen():
    x = yield
    print x

if __name__ == '__main__':
    gen = gen()
    gen.next()
    gen.send(1)
    gen.send(2)
    gen.send(3)