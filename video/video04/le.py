def search(f):
    x = 1
    while True:
        if f(x):
            return x
        x += 1

def inverse(f):
    """返回一个函数g，g(f(x)) = x"""
    return lambda y: search(lambda x: f(x) == y)

def square(x):
    return x * x
