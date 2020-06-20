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
		'Caotangsi', 'Caotangsi', 'Shahepu', 'US Post'
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

plotColors = [
	'deeppink', 'orange', 'yellow', 'springgreen',
	'deepskyblue', 'blue', 'blueviolet', 'magenta',
]
