# a = input("enter a number: ")
# try:
#   numA = int(a)
#   print(sqr(numA))
# except:
#   print(f"Stop! you entered {a} which is invalid!")

# def sqr(x):
#   return x*x
# a = int(input("enter a number: "))

def div(a, b):
  return a/b

def foo():
  try:
    a = int(input("enter a number: "))
    b = int(input("enter a non-zero number: "))
    print(a/b)
  # except ValueError:
  #   print("invalid value")
  #   return
  # except ZeroDivisionError:
  #   print("divisor is zero!")
  #   return
  # except:
  #   print("wrong")
  #   return
  finally:
    print("This is always going to be executed!!!")

foo()