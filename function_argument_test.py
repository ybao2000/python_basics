a = 3
b = 4
c = 5
# def print(args, sep=" ", end="\r\n")  # \r --> carriage return \n  --> new line

print(a, b, c)

s1 = "holy holy holy"
s2 = "molly molly molly"
print(f"{s2}\r{s1}")

print("--------------------")
# default argument
def forex_price(price, currency="CAD"):
  print(f"{price} {currency}")

forex_price(100, "CAD") # you didn't provide the key, so the system adopt the list way

forex_price(100, "USD") # you didn't provide the key, so the system adopt the list way

forex_price(100) # you didn't provide the key, so the system adopt the list

# function argument is a dictionary
forex_price(currency="USD", price=2000) # you provide the key, so the system adopts the dictionary way