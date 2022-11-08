def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) / 3

res = repeat(g, 5)
print(res)
