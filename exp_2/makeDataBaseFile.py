from fileEnum import *


# 整个写
def writeDB(dataBase):
	with open(dbFileName, 'w', encoding='utf-8') as f:
		for keyName in dataBase:
			f.write(keyName + END_KEY)
			for k, v in dataBase[keyName].items():
				f.write(k + REC_SEP + repr(v) + '\t')  # repr() 返回一个对象的 string 格式
			f.write(END_REC)
		f.write(END_DB)


# 整个读
def readDB(fileName):
	dataBase = {}
	with open(fileName, 'r', encoding='utf-8') as f:
		readContent = f.read()
		validContent = readContent.split(END_DB)[0]
		for validRecord in validContent.split(END_REC)[:-1]:
			valueObj = {}
			recordKey, recordValue = validRecord.split(END_KEY)
			values = recordValue.split('\t')[:-1]  # 分割完有空符在末尾
			for eachValue in values:
				innerKey, innerValue = eachValue.split(REC_SEP)
				valueObj[innerKey] = eval(innerValue)
			dataBase[recordKey] = valueObj
	return dataBase


if __name__ == '__main__':
	from initdata import db

	writeDB(db)
