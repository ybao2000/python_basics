try:
    from string import makestrans
except ImportError:
    maketrans = str.maketrans

from string import ascii_lowercase

#old = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#new = 'bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA'

offset = 2

old_lower = ascii_lowercase
new_lower = old_lower[offset:] + old_lower[:offset]
old = old_lower + old_lower.upper()
new = new_lower + new_lower.upper()

# Create a translate table.
trans = maketrans(old, new)

# Translate your string using trans
# print("abc".translate(trans))
# bcd

f = open("test.txt", "r") # r means read
text = f.read()
f.close()
print(text.translate(trans))