__author__ = 'Mitsui'

def thread1():
    for x in range(4):
        print(yield x)


def thread2():
    for x in range(4, 8):
        yield x


threads=[]
threads.append(thread1())
threads.append(thread2())


def run(threads):
    for t in threads:
        try:
            print t.next()
        except StopIteration:
            pass
        else:
            threads.append(t)

def run_():
    g = thread1()
    g.next()
    g.send(1)
    g.send(2)
    g.send(3)


run(threads)
run_()