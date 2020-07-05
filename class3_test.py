class User:
	# name = 'Alpha'
	# age = 10
	# grade = 5
	# name: str
	# age: int
	# grade: int

	# a special function call __init__ (constructor, initializer)

	def intro(self):
		# name = 'Frank'
		# age = 5
		print(self.name, self.age)

	def __str__(self):
		return f"name: {self.name}, age: {self.age}"

user1 = User()
user1.name = "Bob"
user1.age = 10
user1.grade = 5

print("user1", user1)
