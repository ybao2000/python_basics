class User:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName

  def __str__(self):
    return f"{self.firstName}, {self.lastName}"
    
user1 = User("Frank", "Bao")
print(user1)


user2 = User("Bobby", "Adams")
print(user2)