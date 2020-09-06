def reverse(x):
    y, res = abs(x), 0

    while y != 0:
        res = res * 10 + y % 10
        if res <= -2 ** 31 - 1 or res > 2 ** 31:
            return 0
        y //= 10
    return res if x > 0 else -res

if __name__ == '__main__':
    x = -123456
    a = reverse(x)
    print(a)
