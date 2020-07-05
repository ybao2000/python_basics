# def name(arg1, arg2):
# 	pass

class User:
	name = 'Alpha'
	age = 10

	# all functions inside class need self !!!
	def intro(self):
		# name = 'Frank'
		# age = 5
		print(self.name, self.age)

# you directly change the atrribte inside the class
# use . for class.function
# we also used . for package.module.function

user1 = User()
user1.name = "Bob"
user1.age = 5
user1.intro()

user2 = User()
user2.name = "Amily"
user2.age = 15

# user2.name = "Bob"
user2.intro()
