import matplotlib.pyplot as plt
from pylab import *
#支持中文
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
x = ['05G','10G','15G','20G','25G','30G','35G','40G','45G','50G']
y = [58,59,59,60,60,61,61,62,62,63]
y1 = [149,152,151,154,154,155,157,157,159,160]
plt.plot(x, y, marker='o', label='JSON')
plt.plot(x, y1, marker='*', label='CSV')
plt.legend()
plt.xlabel("不同的数据量",fontproperties=zhfont1) #X轴标签
plt.ylabel("清洗时间",fontproperties=zhfont1) #Y轴标签
plt.title("不同类型数据的清洗时间对比",fontproperties=zhfont1) #标题
plt.show()