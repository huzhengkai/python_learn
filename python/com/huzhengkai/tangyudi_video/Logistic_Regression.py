import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy.random
import time
from sklearn import preprocessing as pp

path = 'data' + os.sep + 'LogiReg_data.txt'
pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
print(type(pdData))
print(pdData.head())
print(pdData.shape)

positive = pdData[pdData['Admitted'] == 1]
negative = pdData[pdData['Admitted'] == 0]

fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')
#plt.show()

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

nums = np.arange(-10, 10, step=1) #creates a vector containing 20 equally spaced values from -10 to 10
fig, ax = plt.subplots(figsize=(12,4))
ax.plot(nums, sigmoid(nums), 'r')



def model(X, theta):
    return sigmoid(np.dot(X, theta.T))
#插入一列，0代表列号，'Ones'代表列标识，1代表插入的值。
pdData.insert(0, 'Ones', 1)

orig_data = pdData.as_matrix()
cols = orig_data.shape[1]
X = orig_data[:,0:cols-1]
Y = orig_data[:,cols-1:cols]

theta = np.zeros([1, 3])

def cost(X, Y, theta):
    left = np.multiply(-Y, np.log(model(X, theta)))
    right = np.multiply(1 - Y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / (len(X))


def gradient(X, Y, theta):
    grad = np.zeros(theta.shape)
    error = (model(X, theta)- Y).ravel()
    for j in range(len(theta.ravel())): #for each parmeter
        term = np.multiply(error, X[:,j])
        grad[0, j] = np.sum(term) / len(X)
    return grad

STOP_ITER = 0
STOP_COST = 1
STOP_GRAD = 2

def stopCriterion(type, value, threshold):
    #设定三种不同的停止策略
    if type == STOP_ITER:        return value > threshold
    elif type == STOP_COST:      return abs(value[-1]-value[-2]) < threshold
    elif type == STOP_GRAD:      return np.linalg.norm(value) < threshold   #矩阵2范数

def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[:, 0:cols-1]
    Y = data[:, cols-1:]
    return X, Y

def descent(data, theta, batchSize, stopType, thresh, alpha):
    #梯度下降求解
    init_time = time.time()
    i = 0 # 迭代次数
    k = 0 # batch
    X, Y = shuffleData(data)
    grad = np.zeros(theta.shape) # 计算的梯度
    costs = [cost(X, Y, theta)] # 损失值
    while True:
        grad = gradient(X[k:k+batchSize], Y[k:k+batchSize], theta)
        k += batchSize #取batch数量个数据
        if k >= n:
            k = 0
            X, y = shuffleData(data) #重新洗牌
        theta = theta - alpha*grad # 参数更新
        costs.append(cost(X, Y, theta)) # 计算新的损失
        i += 1

        if stopType == STOP_ITER:       value = i
        elif stopType == STOP_COST:     value = costs
        elif stopType == STOP_GRAD:     value = grad
        if stopCriterion(stopType, value, thresh): break

    return theta, i-1, costs, grad, time.time() - init_time

def runExpe(data, theta, batchSize, stopType, thresh, alpha):

    theta, iter, costs, grad, dur = descent(data, theta, batchSize, stopType, thresh, alpha)
    name = "Original" if (data[:,1]>2).sum() > 1 else "Scaled"
    name += " data - learning rate: {} - ".format(alpha)
    if batchSize==n: strDescType = "Gradient"  #批量梯度
    elif batchSize==1:  strDescType = "Stochastic" #随机梯度
    else: strDescType = "Mini-batch ({})".format(batchSize) #小批量梯度
    name += strDescType + " descent - Stop: "
    if stopType == STOP_ITER: strStop = "{} iterations".format(thresh)
    elif stopType == STOP_COST: strStop = "costs change < {}".format(thresh)
    else: strStop = "gradient norm < {}".format(thresh)
    name += strStop
    print ("***{}\nTheta: {} - Iter: {} - Last cost: {:03.2f} - Duration: {:03.2f}s".format(
        name, theta, iter, costs[-1], dur))
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(np.arange(len(costs)), costs, 'r')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title(name.upper() + ' - Error vs. Iteration')
    return theta

n=100
#指定迭代次数
#runExpe(orig_data, theta, n, STOP_ITER, thresh=5000, alpha=0.000001)
#根据损失值停止
#runExpe(orig_data, theta, n, STOP_COST, thresh=0.000001, alpha=0.001)
#根据梯度变化停止
#runExpe(orig_data, theta, n, STOP_GRAD, thresh=0.05, alpha=0.001)

#上面都是使用的批量梯度下降

#使用随机梯度下降
# runExpe(orig_data, theta, 1, STOP_ITER, thresh=5000, alpha=0.001)
#调小学习率
# runExpe(orig_data, theta, 1, STOP_ITER, thresh=15000, alpha=0.000002)
#随机梯度下降，速度快，但稳定性差，需要很小的学习率

#下面使用小批量梯度下降
#runExpe(orig_data, theta, 16, STOP_ITER, thresh=15000, alpha=0.001)

#浮动仍然比较大，我们来尝试下对数据进行标准化 将数据按其属性(按列进行)减去其均值，然后除以其方差。最后得到的结果是，对每个属性/每列来说所有数据都聚集在0附近，方差值为1
scaled_data = orig_data.copy()
scaled_data[:, 1:3] = pp.scale(orig_data[:, 1:3])

#runExpe(scaled_data, theta, n, STOP_ITER, thresh=5000, alpha=0.001)

#原始数据，只能达到达到0.61，而我们得到了0.38个在这里！ 所以对数据做预处理是非常重要的

#runExpe(scaled_data, theta, n, STOP_GRAD, thresh=0.02, alpha=0.001)

theta = runExpe(scaled_data, theta, 1, STOP_GRAD, thresh=0.002/5, alpha=0.001)

#随机梯度下降更快，但是我们需要迭代的次数也需要更多，所以还是用batch的比较合适！！

def predict(X, theta):
    return [1 if x >= 0.5 else 0 for x in model(X, theta)]
scaled_X = scaled_data[:,:3]
y = scaled_data[:,3]
predictions = predict(scaled_X, theta)
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]
accuracy = (sum(map(int, correct)) % len(correct))
print('accuracy = {0}%'.format(accuracy))

plt.show()


