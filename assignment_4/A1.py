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


class Admin(User):
	def __init__(self, firstName, lastName, description):
		User.__init__(self, firstName, lastName, description)
		self.privileges = Privileges(["can add post", "can delete post", "can ban user"])

	def showPrivileges(self):
		print("{}'s privileges:".format(self.firstName), end='\n')
		self.privileges.showPrivileges()


class Privileges:
	def __init__(self, privileges):
		self.privileges = privileges

	def showPrivileges(self):
		for privilege in self.privileges:
			print(privilege, end='\n')
