# 超过int范围不行
def reverse(x):
    s = str(abs(x))
    s = s[::-1]
    if x >= 0 and x < 2 ** 31:
        s = int(s)
        return s
    elif x < 0 and x >= -2 ** 31 - 1:
        s = int(s)
        return -s


if __name__ == '__main__':
    x = -123456
    a = reverse(x)
    print(a)
