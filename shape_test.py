class Shape():
  pass

class Rectangle(Shape):
  def __init__(self, w, h):
    self.width = w
    self.height = h

  def area(self):
    return self.width * self.height

rect1 = Rectangle(5, 4)
print(rect1.area())

class Square(Rectangle):
  def __init__(self, s):
    # self.side = s
    super().__init__(s, s)

  # def area(self):
  #   return self.side * self.side

sqrt1 = Square(5)
print(sqrt1.area())
# print(sqr1.side)