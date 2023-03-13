

a = '1'

def foo_one():
    b = 2
    print('foo_one')
    print(locals())
    def foo_two():
        c = 3
        print(a, b, c)
        print('foo_two')
        print(locals())
    foo_two()


# foo_one()

from datetime import datetime
import time





def dec(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper

def dec2(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper


@dec2
@dec
def hello():
    time.sleep(2)
    print('Hello')


print(hello())



def number_generator(start, stop):
    while True:
        for i in range(start, stop + 1):
            yield i


start = int(input())
stop = int(input())
n = int(input())
g = number_generator(start, stop)
for i in range(n):
    print(next(g))
