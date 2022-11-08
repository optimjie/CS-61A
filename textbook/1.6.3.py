"""
为什么需要 function nested ?
1. global内函数太多了。
2. update 和 close 应该是某一种计算特有的。
"""
def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance = 1e-3):
    return abs(x - y) < tolerance

def sqrt(a):  # 计算根号a
    def sqrt_update(guess):
        """
        这里采用 (guess + a / guess) / 2 的原因是：
        相当于求 y = x 与 y = (x + a / x) / 2 的交点，
        即方程 2x = x + a / x 的解，显然为根号a。
        不需要关心具体的迭代方法，更需要关注 nest 的好处。
        """
        return (guess + a / guess) / 2
    def sqrt_approx_eq(guess):
        return approx_eq(guess * guess, a)
    return improve(sqrt_update, sqrt_approx_eq)

print(sqrt(256))
