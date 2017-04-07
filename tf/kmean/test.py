import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 生成测试数据
    # 数据数量
    sampleNo = 10
    mu = 3
    # 二维正态分布
    mu = np.array([[1, 5]])
    Sigma = np.array([[1, 0.5], [1.5, 3]])
    R = np.linalg.cholesky(Sigma)
    srcdata = np.dot(np.random.randn(sampleNo, 2), R) + mu
    plt.plot(srcdata[:, 0], srcdata[:, 1], 'bo')
    plt.show()
