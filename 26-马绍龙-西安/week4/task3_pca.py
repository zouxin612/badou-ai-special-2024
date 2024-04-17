import numpy as np


class CPCA(object):
    '''用PCA求样本矩阵X    计算出K阶降维后的矩阵Z
    Note:请保证输入的样本矩阵X shape=(m, n)，m行样例，n个特征
    '''

    def __init__(self, X, K):  # X,样本矩阵X      K 为X要特征降维成k阶
        self.X = X  # 样本矩阵X
        self.K = K  # K阶降维矩阵的K值
        self.centrX = []  # 矩阵X的中心化后的矩阵
        self.C = []  # 样本集的协方差矩阵C
        self.U = []  # 特征向量矩阵
        self.Z = []  # 降维后的结果

        self.centrX = self._centralized()  # 中心化调用
        self.C = self._cov()  # 计算协方差矩阵
        self.U = self._U()
        self.Z = self._Z()  # Z=XU求得

    def _centralized(self):  # 中心化方法
        print('样本矩阵X:\n', self.X)
        mean = np.array([np.mean(attr) for attr in self.X.T])  # 样本集的特征均值     .T: 这是NumPy数组的一个属性，表示其转置。
        print('样本集的特征均值:\n', mean)
        centrX = self.X - mean  # 样本集的中心化
        print('样本矩阵X的中心化centrX:\n', centrX)
        return centrX  # 新生成的NumPy数组将是一个长度为n 的一维数组，其中每个元素对应原数组 self.X 的一列的平均值。

    def _cov(self):  # 求样本矩阵X的协方差矩阵C
        ns = np.shape(self.centrX)[0]  # 原始特征的行数
        C = np.dot(self.centrX.T, self.centrX) / (ns - 1)  # 样本矩阵的协方差矩阵C
        print('样本矩阵X的协方差矩阵C:\n', C)
        return C

    def _U(self):  # 求特征向量矩阵       求X的降维转换矩阵U, shape=(n,k), n是X的特征维度总数，k是降维矩阵的特征维度
        # 先求X的协方差矩阵C的特征值和特征向量
        a, b = np.linalg.eig(self.C)  # 特征值赋值给a，对应特征向量赋值给b。函数doc：https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.eig.html
        print('样本集的协方差矩阵C的特征值:\n', a)
        print('样本集的协方差矩阵C的特征向量:\n', b)

        ind = np.argsort(-1 * a)  # 给出特征值降序的topK的索引序列
        UT = [b[:, ind[i]] for i in range(self.K)]  # 构建K阶降维的降维转换矩阵U
        U = np.transpose(UT)
        print('%d阶降维转换矩阵U:\n' % self.K, U)
        return U

    def _Z(self):  # 按照Z=XU求降维矩阵Z, shape=(m,k), n是样本总数，k是降维矩阵中特征维度总数
        Z = np.dot(self.X, self.U)
        print('X shape:', np.shape(self.X))
        print('U shape:', np.shape(self.U))
        print('Z shape:', np.shape(Z))
        print('样本矩阵X的降维矩阵Z:\n', Z)
        return Z


X = np.array([[10, 15, 29],
              [15, 46, 13],
              [23, 21, 30],
              [11, 9, 35],
              [42, 45, 11],
              [9, 48, 5],
              [11, 21, 14],
              [8, 5, 15],
              [11, 12, 21],
              [21, 20, 25]])
print('样本集(10行3列，10个样例，每个样例3个特征):\n', X)
pca = CPCA(X, 2)
