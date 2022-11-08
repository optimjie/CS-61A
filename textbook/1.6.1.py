def sum(n, term):
    """
    >>> sum(5, natural)
    15
    >>> sum(100, natural)
    5050
    >>> sum(5, square)
    55
    """
    i, ans = 1, 0
    while i <= n:
        i, ans = i + 1, ans + term(i)
    return ans

def natural(k):
    return k

def square(k):
    return k * k

if __name__ = "__main__":
    import doctset
    doctest.testmod()

