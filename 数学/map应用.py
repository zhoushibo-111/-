from functools import reduce

"""
三元表达式
"""
condition = True
print(1 if condition else 2)

"""
map
"""
list1 = [1, 2, 3, 4, 5]
r = map(lambda x: x + x, list1)
print(type(r))  # map类型
print(list(r))
"""
reduce
"""
f = lambda x, y: x + y
r = reduce(f, [1, 2, 3, 4, 5], 10)  # 10是初始化的值
print(r)

# 三大推导式 根据已有的列表推导出新的列表
"""
列表推导式
"""
list2 = [i * i for i in list1]
print(list2)
list3 = [i ** 3 for i in list1]
print(list3)

# 有选择性的筛选
list4 = [i + i for i in list1 if i > 3]
print(list4)
"""
集合推导式
"""
list5 = {1, 2, 3, 4, 5}
list6 = [i + i for i in list5 if i > 3]
print(list6)
"""
字典推导式
"""
s = {
    "zhangsan": 20,
    "lisi": 15,
    "wangwu": 31
}
s_key = [key for key, value in s.items()]
print(s.items())
s_key = {key:value for key, value in s.items() if value==20}
print(s_key)