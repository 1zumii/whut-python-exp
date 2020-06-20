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
			print(np.array(data))


if __name__ == '__main__':
	matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
	matplotlib.rcParams['axes.unicode_minus'] = False  # 和负号正常显示
	main()
