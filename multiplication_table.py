print("mutliplication table:")

for row in range(1, 10):
    for col in range(1, row+1):
        print(f"{row} \u2715 {col}={row*col:3d}", end='  ')
    print()
    print()