__author__ = 'Mitsui'

def str(gen):
    for i in gen:
        print i

if __name__ == '__main__':
    str(x for x in range(1, 10))
    str(x for x in range(1, 10) if x > 5)
    str(x*y for x in range(1, 10) if x > 6 for y in range(11, 20) if y > 15)