class User:
	def __init__(self, firstName, lastName, description):
		self.firstName = firstName
		self.lastName = lastName
		self.description = description
		self.loginAttempts = 0

	def describeUser(self):
		print('{} {}: {}'.format(self.firstName, self.lastName, self.description))

	def greetUser(self):
		print('Hello {} !'.format(self.firstName))

	def incrementLoginAttempts(self):
		self.loginAttempts += 1

	def resetLoginAttempts(self):
		self.loginAttempts = 0