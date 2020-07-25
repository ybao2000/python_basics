class Animal:
  def __init__(self, name):
    self.name = name
  
class Crawler(Animal):
  def __init__(self, name, legs):
    self.name = name
    self.legs = legs

  def crawl(self):
    print(f"{self.name} crawls with {self.legs} legs")

  def eat(self, food):
    print(f"{self.name} swallows {food}")

class Swimmer(Animal):
  def __init__(self, name, size):
    self.name = name
    self.size = size
  
  def swim(self):
    print(f"{self.name} swims")

  def eat(self, food):
    print(f"{self.name} gobbles {food}")

class Snake(Crawler, Swimmer):
  def __init__(self, name, size, legs):
    super().__init__(name, size)
    self.legs = legs

rattle_snake = Snake("Rattle Snake", 10, 0)
rattle_snake.crawl()
rattle_snake.swim()
rattle_snake.eat("rat")

spider = Crawler("Spider", 8)
spider.crawl()
# spider.swim()
spider.eat("mosquitos")

fish = Swimmer("Fish", 5)
fish.eat("flies")

print(Snake.__mro__)