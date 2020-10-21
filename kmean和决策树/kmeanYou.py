from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    data = np.array([[2, 10], [2, 5], [8, 4], [5, 8],
                  [7, 5], [6, 4], [1, 2], [4, 9]])
    sse = []
    for i in range(1,9):
        mid = KMeans(n_clusters=i,init="random",n_init=10,
                     max_iter=200)
        mid.fit(data) # 告诉他可以开始执行了
        sse.append(mid.inertia_)
    plt.plot(range(1,9),sse,marker='o') #marker是画笔
    plt.xlabel("k")
    plt.ylabel("SSE")
    plt.show()
