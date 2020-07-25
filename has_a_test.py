class Course:
  def __init__(self, name, description):
    self.name = name
    self.description = description

course1 = Course("Python Basics", "this is a introduction")
print(course1)


class Student:
  def __init__(self, firstName, lastName, course):
    self.firstName = firstName
    self.lastName = lastName
    self.course = course

student1 = Student("Bobby", "Adams", course1)
print(student1)
print(student1.course.name)
