class Person:
	def __init__(self, name, age, pay=0, job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)


if __name__ == '__main__':
	p1 = Person('a1', 11, 200, 'py')
	p2 = Person('a2', 12, 202, 'py')
	print(p1.lastName())
	print(p2.lastName())
	print(p1.pay)
	print(p2.pay)
	p1.giveRaise(0.5)
	p2.giveRaise(0.6)
	print(p1.pay)
	print(p2.pay)
