import numpy as np

# 使用random模块来随机生成2000个0,1的值（掷硬币值）（两个结果任选一个），利用函数使0变成-1
vector = np.random.choice([0, 1], 2000)
vector[vector == 0] = -1

# 使用cumsum()函数累计步数和，显示酒鬼每一步距原点的距离
distanceSum = vector.cumsum() * 0.5
print('每一步距原点的距离(米):', distanceSum)

# 找出酒鬼离原点正向最远、反向最远距离
print('距离原点正向最远：{}米'.format(distanceSum[distanceSum.argmax()]))
print('距离原点反向最远：{}米'.format(distanceSum[distanceSum.argmin()]))

# 当酒鬼距原点的距离大于或等于15米时，总共走了多少步？如果没有走到15米，请输出：'酒鬼最远也没走到15米'
count = 0
if all(abs(i) < 15 for i in distanceSum):
	print('最远也没走到15米')
else:
	for i in distanceSum:
		count += 1
		if i == 15 or i == -15:
			break
	print('首次大于或等于15米时，所走的步数：', count)
