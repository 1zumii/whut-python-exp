from Person import Person


class Manager(Person):
	def giveRaise(self, percent, bonus=0.1):
		self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
	m1 = Manager('k1', 50, 600, 'py')
	print(m1.pay)
	m1.giveRaise(0.5)
	print(m1.pay)
