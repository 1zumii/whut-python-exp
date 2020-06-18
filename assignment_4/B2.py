from B1 import User


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
