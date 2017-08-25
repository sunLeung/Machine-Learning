import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print(iris_X[:2, :])
print(iris_y)

# 生成训练集、预测集
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

predict = knn.predict(X_test)
np.savetxt('predict.cvs', predict, delimiter=',')
np.savetxt('ytest.cvs', y_test, delimiter=',')
