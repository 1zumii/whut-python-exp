BeiJingFile = 'BeijingPM20100101_20151231.csv'
ChengDuFile = 'ChengduPM20100101_20151231.csv'
GuangZhouFile = 'GuangzhouPM20100101_20151231.csv'
ShangHaiFile = 'ShanghaiPM20100101_20151231.csv'
ShenYangFile = 'ShenyangPM20100101_20151231.csv'

cityNameDict = {
	'beijing': '北京',
	'chengdu': '成都',
	'guangzhou': '广州',
	'shanghai': '上海',
	'shenyang': '沈阳'
}

districtNameDict = {
	'Dongsi': '东西',
	'Dongsihuan': '东四环',
	'Nongzhanguan': '农展馆',
	'US Post': '美国大使馆',
	'Caotangsi': '草堂寺',
	'Shahepu': '沙河铺',
	'City Station': '市监测站',
	'5th Middle School': '第五中学',
	'Jingan': '静安监测站',
	'Xuhui': '徐汇上师大',
	'Taiyuanjie': '太原街',
	'Xiaoheyan': '小河沿'
}

dataConfigDict = {
	'beijing': (BeiJingFile, [
		'Dongsi', 'Dongsihuan', 'Nongzhanguan', 'US Post'
	]),
	'chengdu': (ChengDuFile, [
		'Caotangsi', 'Shahepu', 'US Post'
	]),
	'guangzhou': (GuangZhouFile, [
		'City Station', '5th Middle School', 'US Post'
	]),
	'shanghai': (ShangHaiFile, [
		'Jingan', 'US Post', 'Xuhui'
	]),
	'shenyang': (ShenYangFile, [
		'Taiyuanjie', 'US Post', 'Xiaoheyan'
	])
}

plotContrastColors = [
	'deeppink', 'deepskyblue', 'yellow', 'blueviolet',
	'orange', 'blue', 'magenta', 'springgreen'
]
plotGradientColors = [
	'deepskyblue', 'springgreen', 'yellow', 'deeppink'
]

seasonName = [
	'春', '夏', '秋', '冬'
]

seasonMap = [
	[3, 4, 5],  # 第一季度
	[6, 7, 8],  # 第二季度
	[9, 10, 11],  # 第三季度
	[12, 1, 2]  # 第四季度
]
