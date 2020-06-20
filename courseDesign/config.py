BeiJingFile = 'BeijingPM20100101_20151231.csv'
ChengDuFile = 'ChengduPM20100101_20151231.csv'
GuangZhouFile = 'GuangzhouPM20100101_20151231.csv'
ShangHaiFile = 'ShanghaiPM20100101_20151231.csv'
ShenYangFile = 'ShenyangPM20100101_20151231.csv'

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
