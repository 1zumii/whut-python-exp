import pickle

with open('sue.pkl', 'rb+') as f:
	sue = pickle.load(f)
	print(sue['pay'])
	sue['pay'] *= 1.1
	print(sue['pay'])
	pickle.dump(sue, f)
