
from numpy import *
import operator

#使用的欧氏距离，也可以使用其他距离
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVector
#把datingTestSet2.txt中的数据分成测试数据和测试结果两个部分
returnMat,classLabelVector = file2matrix("datingTestSet2.txt")
print(returnMat)
print(classLabelVector)

def autoNorm(dataSet):
    #每一列的最小值,是一个1*n的矩阵
    minVals = dataSet.min(0)
    #每一列的最大值,是一个1*n的矩阵
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10      #hold out 10%
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')       #load data setfrom file
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    print(numTestVecs)
    errorCount = 0.0
    for i in range(numTestVecs):
        #normMat[i,:]为测试数据，normMat[numTestVecs:m,:]为训练数据
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    print(errorCount)

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']         #可能输出的结果
    percentTats = float(input("percentage of time spent playing video games?")) #输入看电影的时间
    ffMiles = float(input("frequent flier miles earned per year?"))   #坐飞机时间
    iceCream = float(input("liters of ice cream consumed per year?")) #吃冰淇淋公升数
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')        #读取样本
    normMat,ranges,minVals = autoNorm(datingDataMat)                      #归一化
    inArr = array([ffMiles,percentTats,iceCream])                       #输入样本
    #我们同样需要对输入样本进行归一化的处理
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("You will probably like this person: ",resultList[classifierResult -1]) #数据标签是1,2,3，因此要减1

classifyPerson()