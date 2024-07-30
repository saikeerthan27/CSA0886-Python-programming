rows = 3
k = 0
for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print("  ", end="")
    while k != (2 * i - 1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
rows = rows - 1
k = 0
for i in range(rows, 0, -1):
    for space in range(0, rows - i):
        print("  ", end="")
    k = 0
    while k != (2 * i - 1):
        print("* ", end="")
        k = k + 1
    print()
