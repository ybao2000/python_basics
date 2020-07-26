f = open("test.txt", "r") # r means read
text = f.read()
f.close()

decode = []
for ch in text:
  if ch == ".":
    decode.append(ch)
  else:
    num = ord(ch)
    if num > ord('x'):
      num -= 26
    dch = chr(num+2)
    decode.append(dch)

print(''.join(decode))


# a -> c
# b -> d
# ....
# x -> z
# y -> z next => a!!!
# z -> b