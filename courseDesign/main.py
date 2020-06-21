import config
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 一个城市六年的污染情况
def pollutingCondition(cityName, districtList, reader):
	# 获取每个区的整列数据
	year = np.array(reader.year)
	month = np.array(reader.month)
	data = []
	for district in districtList:
		districtSum = []
		currentDistrictData = np.array(reader['PM_' + district])  # 访问DataFrame指定列的字符串方式
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
	plt.figure(figsize=(16, 10))  # 设置画布大小 // 16:10 分辨率默认100 => 1600×1000 ?
	for plotIndex in range(1, (year[-1] - year[0] + 1) + 1):  # 年份
		plt.subplot(2, 3, plotIndex)
		x = range(1, 12 + 1)
		for districtIndex in range(0, len(districtList)):
			# 画每个子图种不同区数据的折线
			plt.plot(  # 折线图
				x, dataArr[districtIndex, plotIndex - 1],
				color=config.plotContrastColors[districtIndex],
				label=config.districtNameDict[districtList[districtIndex]]
			)
			plt.plot(  # 散点图
				x, dataArr[districtIndex, plotIndex - 1], 'ob',
				color=config.plotContrastColors[districtIndex]
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
	plt.suptitle(config.cityNameDict[cityName])  # 画完子图，写大标题
	plt.savefig('./output/PollutingCondition_{}_6year.png'.format(cityName))


# 按月度画每个城市中各个区的百分比柱状图
def airQualityByMonth(cityName, districtList, reader):
	# 获取每个区的整列数据
	month = np.array(reader.month)
	data = []
	for district in districtList:
		districtSum = []
		currentDistrictData = np.array(reader['PM_' + district])
		for monthIndex in range(1, 13):
			# 所有数据中，同一个区，同一个月时的数据
			monthArr = currentDistrictData[month == monthIndex]
			# 筛选出非np.nan的数据，对np.isnan()取反
			# 此时validData中的长度和索引就和源数据不相同了
			validData = monthArr[~np.isnan(monthArr)]
			districtSum.append([  # 单月数据
				len(validData[validData <= 35]),  # 优良
				len(validData[(validData > 35) & (validData <= 75)]),  # 轻度
				len(validData[(validData > 75) & (validData <= 150)]),  # 中度
				len(validData[validData > 150])  # 重度
			])
		data.append(districtSum)  # append单个区，按月份分的数据
	dataArr = np.array(data)
	# 月度
	plt.figure(figsize=(16, 10))
	for districtIndex in range(0, len(districtList)):
		plt.subplot(2, 2, districtIndex + 1)
		for monthIndex in range(1, 13):
			# 子图中的单列
			sumCount = dataArr[districtIndex, monthIndex - 1].sum()
			percentGood = dataArr[districtIndex, monthIndex - 1][0] / sumCount
			percentMild = dataArr[districtIndex, monthIndex - 1][1] / sumCount
			percentMedium = dataArr[districtIndex, monthIndex - 1][2] / sumCount
			percentSevere = dataArr[districtIndex, monthIndex - 1][3] / sumCount
			plt.bar(
				monthIndex, percentGood,
				width=0.4, label='优良空气',
				color=config.plotGradientColors[0],
				bottom=0
			)
			plt.bar(
				monthIndex, percentMild,
				width=0.4, label='轻度污染',
				color=config.plotGradientColors[1],
				bottom=percentGood
			)
			plt.bar(
				monthIndex, percentMedium,
				width=0.4, label='中度污染',
				color=config.plotGradientColors[2],
				bottom=percentGood + percentMild
			)
			plt.bar(
				monthIndex, percentSevere,
				width=0.4, label='重度污染',
				color=config.plotGradientColors[3],
				bottom=percentGood + percentMild + percentMedium
			)
		# y轴取值范围
		plt.ylim(0, 1.0)
		# 设置x轴刻度显示值
		# 参数一：中点坐标; 参数二：显示值
		plt.xticks(range(1, 13), range(1, 13))
		plt.xlabel('月份')
		# 设置标题
		plt.title(config.districtNameDict[districtList[districtIndex]])
	# 设置题注
	# plt.legend()
	plt.suptitle(config.cityNameDict[cityName])  # 画完子图，写大标题
	plt.savefig('./output/AirQuality12month_{}_byDistrict.png'.format(cityName))


# 按季度画每个城市中各个区的百分比柱状图
def airQualityBySeason(cityName, districtList, reader):
	# 获取每个区的整列数据
	season = np.array(reader.season)
	data = []
	for district in districtList:
		districtSum = []
		currentDistrictData = np.array(reader['PM_' + district])
		for seasonIndex in range(0, len(config.seasonMap)):
			# 所有数据中，同一个区，同一个季度时的数据
			seasonArr = currentDistrictData[season == seasonIndex + 1]
			# 筛选出非np.nan的数据，对np.isnan()取反
			# 此时validData中的长度和索引就和源数据不相同了
			validData = seasonArr[~np.isnan(seasonArr)]
			districtSum.append([  # 单季度数据
				len(validData[validData <= 35]),  # 优良
				len(validData[(validData > 35) & (validData <= 75)]),  # 轻度
				len(validData[(validData > 75) & (validData <= 150)]),  # 中度
				len(validData[validData > 150])  # 重度
			])
		data.append(districtSum)  # append单个区，按季度分的数据
	dataArr = np.array(data)
	# 季度
	plt.figure(figsize=(16, 10))
	for districtIndex in range(0, len(districtList)):
		plt.subplot(2, 2, districtIndex + 1)
		for seasonIndex in range(0, len(config.seasonName)):
			# 子图中的单列
			sumCount = dataArr[districtIndex, seasonIndex].sum()
			percentGood = dataArr[districtIndex, seasonIndex][0] / sumCount
			percentMild = dataArr[districtIndex, seasonIndex][1] / sumCount
			percentMedium = dataArr[districtIndex, seasonIndex][2] / sumCount
			percentSevere = dataArr[districtIndex, seasonIndex][3] / sumCount
			plt.bar(
				seasonIndex + 1, percentGood,
				width=0.4, label='优良空气',
				color=config.plotGradientColors[0],
				bottom=0
			)
			plt.bar(
				seasonIndex + 1, percentMild,
				width=0.4, label='轻度污染',
				color=config.plotGradientColors[1],
				bottom=percentGood
			)
			plt.bar(
				seasonIndex + 1, percentMedium,
				width=0.4, label='中度污染',
				color=config.plotGradientColors[2],
				bottom=percentGood + percentMild
			)
			plt.bar(
				seasonIndex + 1, percentSevere,
				width=0.4, label='重度污染',
				color=config.plotGradientColors[3],
				bottom=percentGood + percentMild + percentMedium
			)
		# y轴取值范围
		plt.ylim(0, 1.0)
		# 设置x轴刻度显示值
		# 参数一：中点坐标; 参数二：显示值
		plt.xticks(range(1, len(config.seasonName) + 1), config.seasonName)
		plt.xlabel('季度')
		# 设置标题
		plt.title(config.districtNameDict[districtList[districtIndex]])

	plt.suptitle(config.cityNameDict[cityName])  # 画完子图，写大标题
	plt.savefig('./output/AirQuality4season_{}_byDistrict.png'.format(cityName))


def main():
	for cityName, (fileName, districtList) in config.dataConfigDict.items():
		csvReader = pd.read_csv('./data/' + fileName)
		# 五城市污染状态
		pollutingCondition(cityName, districtList, csvReader)
		# 五城市每个区空气质量的月度差异
		airQualityByMonth(cityName, districtList, csvReader)
		# 五城市每个区空气质量的季度差异
		airQualityBySeason(cityName, districtList, csvReader)


if __name__ == '__main__':
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
	matplotlib.rcParams['axes.unicode_minus'] = False  # 和负号正常显示
	main()
