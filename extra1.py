def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

for a in fib():
    print(a, end="\n")