import numpy as np
import csv
import config


def main():
	csvFile = open('./data/' + config.BeiJingFile, 'r')
	csvReader = csv.reader(csvFile)
	for line in csvReader:
		if csvReader.line_num is 1:
			print(line)
		elif csvReader.line_num is 2:
			print(line)
		else:
			break


if __name__ == '__main__':
	main()
