import numpy as np


class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        """
        eta: 学习率
        n_iter: 权重向量的训练次数
        w_: 神经元分叉权重向量
        errors_: 用于记录神经元判断出错次数
        """
        self.eta = eta
        self.n_iter = n_iter
        self.w_ = []
        self.errors_ = []
        pass

    def fit(self, x, y):
        """
        输入训练数据，训练神经元
        :param x: 输入样本向量
        :param y: 对应样本分类
        X:shape[n_samples,n_features]
        X:[[1,2,3],[4,5,6]]
        n_samples:2
        n_features:3
        y:[1,-1]
        初始化权重向量为0
        加一是因为前面提到的w0，也就是激活函数阀值
        """
        self.w_ = np.zero(1 + x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(x, y):

                pass
            pass

        pass
