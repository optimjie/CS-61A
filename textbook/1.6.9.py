def trace1(func):
    def traced(x):
        print('Calling', func, 'on argument', x)
        return func(x)
    return traced

# @trace1
def square(x):
    return x * x;

print(trace1(square)(5))

print(square(5))
