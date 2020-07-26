# lambda function  2, one line of code
#  -- 1, anonymouse funciton (no function name)
#  -- 2, only one line of code
#  -- 3, defined when it is use (regular function is defined first, then use it later)

def foo(x):
  return x % 3 == 0

# mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

mult3 = filter(foo, [1, 2, 3, 4, 5, 6, 7, 8, 9])

for item in mult3:
  print(item)


#Given a list of names, return the list of length of the names
def get_lens(names):
  l = []
  for name in names:
    l.append(len(name))
  return l

names = ["Frank", "Alpha", "Beta", "Bobby", "Abby", "Jemery", "Hughs"]

# => [5, 5, 4, 5, 4, 6, 5]

print(get_lens(names))

# def myfunc(n):
#   return len(n)

# print(list(map(myfunc, names)))

print(list(map(lambda x: len(x), names)))
