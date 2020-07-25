class Course:
  def __init__(self, name, description):
    self.name = name
    self.description = description

course1 = Course("Python Basics", "this is a introduction")
print(course1)

class User:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName

class Student(User):
  def __init__(self, firstName, lastName, course, grade):
    # use super() to find Parent, call Parent's __init__
    super().__init__(firstName, lastName)
    self.course = course
    self.grade = grade

class Teacher(User):
  pass

class Admin(User):
  pass

student1 = Student("Bobby", "Adams", course1, 80)
print(student1)
print(student1.course.name)

teacher1 = Teacher("Frank", "Bao")