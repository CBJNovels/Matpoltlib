import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.scatter(x_values, y_values, s=100)
# # s为点的大小

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
# c为颜色显示,edgecolors蓝色实心点显示

#颜色映射
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=40)

#设置图标标题，并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
#x(0-1100),y(0-1,100,000)

#自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()