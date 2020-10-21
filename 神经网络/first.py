import numpy as np
import pandas as pd
from second import *
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.axes._axes import _log as matplotlib_axes_logger

matplotlib_axes_logger.setLevel('ERROR')


class Perception(object):
    '''
    eta: 学习率
    n_iter:权重向量的训练次数
    w_: 神经网络权重向量
    errors_:用于记录神经元判断出错次数
    '''

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        pass

    def fit(self, X, y):
        '''
        输入训练数据，X是输入样本，y是对应样本分类
        要使用 shape
        '''
        # 初始化向量权重为0 初始化时要把步调函数的阈值当做第0个分量
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                """
                w(1) = x[1]*update,w(2)*update
                w[1:] 我们把第一位w(0)设为阈值  权重在后面三个
                """
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
                self.errors_.append(errors)

    def net_input(self, X):
        """
        z=w0*1+w1*x1+...+Wn*Xn
        """
        return np.dot(X, self.w_[1:] + self.w_[0])

    def predict(self, X):
        """
        辨别如果算出z大于0 则为1 否则为-1
        """
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    def plot_decision_regions(X, y, classifier, resolution=0.02):
        markers = ('s', 'x', 'c', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max()
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max()
        # print(x1_min, x1_max)
        # print(x2_min, x2_max)
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))

        # print(xx1.shape)
        # print(xx1)
        z = classifier.predict(np.array([xx1.ravel(),
                                         xx2.ravel()]).T)
        print(xx1.ravel())
        print(xx2.ravel())
        print(z)
        z = z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        for idx, c1 in enumerate(np.unique(y)):
            plt.scatter(x=X[y == c1, 0], y=X[y == c1, 1], alpha=0.8, c=cmap(idx),
                        marker=markers[idx], label=c1)


if __name__ == '__main__':
    file = 'D:\pythonJZZX\ShuJuJieGou\\test.csv'
    df = pd.read_csv(file, header=None)
    # 把 1-1000条数据的第四列抽取出来
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    x = df.iloc[0:100, [0, 2]].values
    plt.scatter(x[:50, 0], x[:50, 1], color='red', marker='o', label='setosa')
    plt.scatter(x[50:100, 0], x[50:100, 1], color='blue', marker='x', label='versicolor')
    plt.xlabel('花瓣长度')
    plt.ylabel('花径长度')
    plt.legend(loc='upper left')
    # plt.show()
    ppn = Perception(eta=0.1, n_iter=10)
    ppn.fit(x, y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('错误分类次数')
    # plt.show()
    Perception.plot_decision_regions(x, y, ppn, resolution=0.02)
    plt.xlabel('花瓣长度')
    plt.ylabel('花径长度')
    plt.legend(loc='upper left')
    #plt.show()
    ada = AdalineGD(eta=0.0001, n_iter=50)
    ada.fit(x, y)
    Perception.plot_decision_regions(x, y, classifier=ada)
    plt.title('Adaline-Gradient descent')
    plt.xlabel('huajing length')
    plt.ylabel('huaban length')
    plt.legend(loc='upper left')
    # plt.show()
    plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('sum-squard-error')
    plt.show()
