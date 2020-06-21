import config
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
	for cityName, (fileName, districtList) in config.dataConfigDict.items():
		csvReader = pd.read_csv('./data/' + fileName)
		if fileName is config.BeiJingFile:
			# 获取每个区的整列数据
			year = np.array(csvReader.year)
			month = np.array(csvReader.month)
			data = []
			for district in districtList:
				districtSum = []
				currentDistrictData = np.array(csvReader['PM_' + district])  # 访问DataFrame指定列的字符串方式
				for yearIndex in range(year[0], year[-1] + 1):
					for monthIndex in range(1, 13):
						monthArr = currentDistrictData[(year == yearIndex) & (month == monthIndex)]
						# 筛选出非np.nan的数据，对np.isnan()取反
						validData = monthArr[~np.isnan(monthArr)]
						if len(validData) is 0:
							districtSum.append(np.nan)
						else:
							districtSum.append(np.mean(validData))
				data.append(np.array(districtSum).reshape(
					len(range(year[0], year[-1] + 1)),  # row
					12  # column
				))
			# dataArr.shape = (4个区,6年,12个月)
			# [
			# 	[2010,2011,2012,2013,2014,2015],
			# 	... ...
			# 	[2010,2011,2012,2013,2014,2015],
			# ]
			dataArr = np.array(data)
			# 绘制条形图，按年份
			plt.figure(figsize=(8, 5))  # 设置画布大小 // 16:10 分辨率默认100 => 1600×1000 ?
			for plotIndex in range(1, (year[-1] - year[0] + 1) + 1):  # 年份
				plt.subplot(2, 3, plotIndex)
				x = range(1, 12 + 1)
				for districtIndex in range(0, len(districtList)):
					# 画每个子图种不同区数据的折线
					plt.plot(  # 折线图
						x, dataArr[districtIndex, plotIndex - 1],
						color=config.plotColors[districtIndex],
						label=config.districtNameDict[districtList[districtIndex]]
					)
					plt.plot(  # 散点图
						x, dataArr[districtIndex, plotIndex - 1], 'ob',
						color=config.plotColors[districtIndex]
					)
					# y轴取值范围
					plt.ylim(0, 200)
					plt.ylabel("PM 2.5")
					# 设置x轴刻度显示值
					# 参数一：中点坐标; 参数二：显示值
					plt.xticks(x, x)
					plt.xlabel('月份')
					# 设置标题
					plt.title(plotIndex + year[0] - 1)
					# 设置题注
					plt.legend()
			plt.savefig('./output/{}.png'.format(cityName))


if __name__ == '__main__':
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
	matplotlib.rcParams['axes.unicode_minus'] = False  # 和负号正常显示
	main()
