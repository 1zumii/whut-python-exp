import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

rowTitle = [5, 10, 20, 50, 100]  # 横着的
columnTitle = ['Freeze', 'Wind', 'Flood', 'Quake', 'Hail']  # label分类
colors = ['deeppink', 'orange', 'yellow', 'springgreen', 'deepskyblue']
data = [  # 竖着的值
	[66386, 58230, 89135, 78415, 139361],
	[174296, 381139, 80552, 81858, 331509],
	[75131, 78045, 152558, 150656, 343164],
	[577908, 99308, 497981, 193263, 781380],
	[32015, 160454, 603535, 69638, 52269]
]
xBase = range(0, len(columnTitle) * 2, 2)
xWidth = 0.3
rectangles = []
# 绘制条形图
for index in range(len(columnTitle)):
	rectangles.append(plt.bar(
		x=[i + index * xWidth for i in xBase], height=data[index],
		width=xWidth, color=colors[index], label=columnTitle[index]
	))
# y轴取值范围
plt.ylim(
	min(map(lambda arr: min(arr), data)) - 30000,
	max(map(lambda arr: max(arr), data)) + 50000
)
plt.ylabel("数量")

# 设置x轴刻度显示值
# 参数一：中点坐标
# 参数二：显示值
plt.xticks([i + (xWidth * len(columnTitle) / 2) for i in xBase], rowTitle)
plt.xlabel("年份")
plt.title("各时间段的发生的灾害数量")
# 设置题注
plt.legend()
# 编辑文本
for recArr in rectangles:
	for rec in recArr:
		height = rec.get_height()
		plt.text(
			rec.get_x() + rec.get_width() / 2,
			height + 10000, str(height),
			ha="center", va="bottom"
		)
plt.show()
