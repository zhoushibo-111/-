import sympy as sp

x = sp.Symbol('x')
y1 = 3 * x
f1 = sp.diff(y1)

y2 = 1 / x
# 求导
f2 = sp.diff(y2)
# 积分
F2 = sp.integrate(y2, x)
print(x)
print(f2)
print(F2)
# 求极限
L1 = sp.limit(y2,x,0)
print(L1)
