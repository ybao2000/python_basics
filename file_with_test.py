lines = []
with open("test.txt", "r") as f:
  for line in f:
    lines.append(line)

print(lines)