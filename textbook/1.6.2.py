"""
其实就是 y = x 与 y = 1/x + 1 的交点位置，
即方程 x^2 = x + 1 的解
"""
def improve(update, close, guess = 1):
    """
    update 就是用于迭代猜的值
    close 判断猜的值是否满足精度的要求
    只不过这里的 close 和 update 都是函数罢了
    """
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1 / guess + 1

def golden_approx_eq(guess):
    return approx_eq(guess * guess, 1 + guess)

def approx_eq(x, y, tolerance = 1e-3):  # x与y的差距不超过tolerance
    return abs(x - y) < tolerance

phi = improve(golden_update, golden_approx_eq)
print(phi)
