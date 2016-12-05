__author__ = 'Mitsui'


class bean(object):
    @classmethod
    def foo(cls, **args):
        print('class = %s and args = %s' % (cls, args))

    @staticmethod
    def bar(**args):
        print('static args = %s' % args)


if __name__ == '__main__':
    bean.foo(name='Ethan')
    bean().foo(name='Ethan')
    bean.foo()

    bean.bar(msg='hehe')
