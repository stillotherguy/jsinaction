__author__ = 'Mitsui'

def str(enu):
    for key, value in enu:
        print key,value

if __name__ == '__main__':
    str(enumerate(['a', 'b', 'c', 'd']))
    str(enumerate(['a', 'b', 'c', 'd'], start=1))
    str(enumerate(dict([('name', 'Ethan')], age=29)))
    str({'name' : 'Ethan'}.items())