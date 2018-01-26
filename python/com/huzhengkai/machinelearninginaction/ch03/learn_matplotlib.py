import matplotlib.pyplot as plt
import pandas
import numpy as np

# weight = [600,150,200,300,200,100,125,180]
# height = [60,65,73,70,65,58,66,67]
# plt.scatter(height, weight)
# plt.show()

forest_fires = pandas.read_csv('forest_fires.csv')

print(forest_fires.head(5))

#以风速数据（wind）作为x轴，烧毁面积（area）作为y轴，做出它们的散点图
# plt.scatter(forest_fires["wind"], forest_fires["area"])
# plt.title('Wind speed vs fire area')
# plt.xlabel('Wind speed when fire started')
# plt.ylabel('Area consumed by fire')
# plt.show()


# 使用列表数据作为坐标轴
# age = [5, 10, 15, 20, 25, 30]
# height = [25, 45, 65, 75, 75, 75]
# plt.plot(age, height)
# plt.title('Age vs Height')
# plt.xlabel('age')
# plt.ylabel('Height')
# plt.show()

print("--------------------")
# 现在要按月份统计烧毁的面积
# 先做一个透视图，计算每个月的烧毁面积
area_by_month = forest_fires.pivot_table(index="month", values="area", aggfunc=np.sum)
print(area_by_month)
plt.bar(range(len(area_by_month)), area_by_month)
plt.title('Month vs Area')
plt.xlabel('month')
plt.ylabel('area')
plt.show()


# 定义决策树决策结果的属性，用字典来定义
# 下面的字典定义也可写作 decisionNode={boxstyle:'sawtooth',fc:'0.8'}
# boxstyle为文本框的类型，sawtooth是锯齿形，fc是边框线粗细
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
# 定义决策树的叶子结点的描述属性
leafNode = dict(boxstyle="round4", fc="0.8")
# 定义决策树的箭头属性
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )

def createPlot():
   fig = plt.figure(1, facecolor='white')
   fig.clf()
   createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
   plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
   plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
   plt.show()





