import random
from matplotlib import pyplot as plt
import numpy

font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': '12'}
plt.rc("font", **font)
plt.rc("font", family='MicroSoft YaHei', weight='bold', size='12')
x = range(60)
x_ticks = ["11点{}分".format(i) for i in x]
y = [random.uniform(10,15) for i in x]

plt.figure(figsize=(20, 8), dpi=100)
plt.xticks(_x[::5], _x_label[::5], rotation=45)
plt.plot(x_ticks, y)
y_ticks = range(40)
plt.yticks(y_ticks)
plt.show()
# a = "{}python{}".format("1","2")
# print(a)
