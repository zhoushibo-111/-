from first import *
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.axes._axes import _log as matplotlib_axes_logger


class AdalineGD(object):
    """
    eta: float  学习效率 0-1
    n_iter: int
    对训练数据进行学习改进
    w 权重
    error 判断错误的次数
    """

    def __init__(self, eta=0.01, n_iter=50):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        X  里面有 n_samples 表示X中含有训练数据条数
                n_features 其中一条训练数据
        y 用于存储每一训练条数对应的正确分类
        """
        self.w_ = np.zeros(1 + X.shape[1])  # X.shape[1] X的列数
        self.cost_ = []
        for i in range(self.n_iter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors ** 2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return self.net_input(X)

    def predict(self, X):
        return np.where(self.activation(X) >= 0, 1, -1)


if __name__ == '__main__':
    # ada = AdalineGD(eta=0.0001, n_iter=50)
    # ada.fit(X, y)
    # Perception.plot_decision_regions(X, y, classifier=ada)
    # plt.title('Adaline-Gradient descent')
    # plt.xlabel('huajing length')
    # plt.ylabel('huaban length')
    # plt.legend(loc='upper left')
    # plt.show()
    # plt.plot(range(1, len(ada.cost_) + 1),ada.cost_,marker='o')
    # plt.xlabel('Epochs')
    # plt.ylabel('sum-squard-error')
    # plt.show()
    pass