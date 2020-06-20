import numpy as np
import pandas as pd
import config


def main():
	for cityName, cityData in config.dataConfigDict.items():
		csvReader = pd.read_csv('./data/' + cityData[0])
		print(cityName, len(csvReader.No))


if __name__ == '__main__':
	main()
