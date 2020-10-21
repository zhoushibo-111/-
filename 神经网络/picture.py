from first import *
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, resolution=0.02):
    marker = ('s', 'x', 'c', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max()
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max()
    print(x1_min, x1_max)
    print(x2_min, x2_max)


if __name__ == '__main__':
    plot_decision_regions()
