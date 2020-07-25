class Shape():
  pass

class Rectangle(Shape):
  def __init__(self, w, h):
    self.width = w
    self.height = h
  
  @property  # a method as attribute for user
  def area(self):
    return self.width * self.height
 
  def inflat(self, multiple):
    self.width = self.width * multiple
    self.height = self.height * multiple

  # @property - no passing parameter, return a value
  # @property
  def inflat_area(self, multiple):
    return self.width * self.height * multiple

rect1 = Rectangle(4, 5)
print(rect1.area)

rect1.inflat(2)
print(rect1.width, rect1.height, rect1.area)

a = rect1.inflat_area(2)
print(a)
