def my_pow(a):
    def f(b):
        return pow(a, b)
    return f

print(my_pow(2)(3))
