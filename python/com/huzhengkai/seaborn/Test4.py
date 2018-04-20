import matplotlib.pyplot as plt
from pylab import *


zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

x = ['05G','10G','15G','20G','25G','30G','35G','40G','45G','50G']

y = [149,152,151,154,154,155,157,157,159,160]

y1 = [205,293,376,504,596,633,793,939,1070,1141]

plt.plot(x, y, marker='o', label='Spark')
plt.plot(x, y1, marker='*', label='MapReduce')

plt.legend()
plt.xlabel("不同的数据量",fontproperties=zhfont1) #X轴标签
plt.ylabel("清洗时间",fontproperties=zhfont1) #Y轴标签
plt.title("Spark与MapReduce清洗时间对比",fontproperties=zhfont1) #标题

plt.show()