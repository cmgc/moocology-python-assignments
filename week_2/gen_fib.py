
def fib_generator(n):
    a, b = 0, 1

    if n < 1: yield 0

    while n > 0:
        yield a
        a, b = b, a+b
        n -= 1

for i in fib_generator(5):
    print i
