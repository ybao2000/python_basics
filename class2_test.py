class User:
	# name = 'Alpha'
	# age = 10
	# grade = 5

	# a special function call __init__ (constructor, initializer)
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade

	def intro(self):
		# name = 'Frank'
		# age = 5
		print(self.name, self.age)

  # display of the class object
	def __str__(self):
		return f"name: {self.name}, age: {self.age}"

user1 = User("Bob", 10, 5)
print("user1", user1)

user2 = User("Amily", 15, 10)
print("user2", user2)