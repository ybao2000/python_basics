class User:
  def __init__(self, username, email):
    self.username = username
    self.email = email

  def intro(self):
    print(f"username: {self.username}, email: {self.email}")

  def write_note(self):
    print(f"{self.username} write note")

user1 = User("Frank", "frank@gmail.com")
user1.intro()
  
class Student(User):
  def __init__(self, username, email, grade):
    super().__init__(username, email)
    self.grade = grade

  # this intro() overrides intro() in parent
  def intro(self):
    print(f"username: {self.username}, email: {self.email}, grade: {self.grade}")

student1 = Student("Alpha", "alpha@gamil.com", 8)
student1.intro()
student1.write_note()