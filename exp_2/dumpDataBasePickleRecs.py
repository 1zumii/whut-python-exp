import glob
import pickle

for filename in glob.glob('*.pkl'):
	flatFile = open(filename, 'rb')
	record = pickle.load(flatFile)
	print(filename, '=>\n ', record)
	flatFile.close()
