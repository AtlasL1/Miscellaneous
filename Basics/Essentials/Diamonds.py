lines = int(input("Enter number of rows: "))

for i in range(1, lines + 1):
    print(" " * (lines - i) + "*" * (2 * i - 1))

for i in range(lines - 1, 0, -1):
    print(" " * (lines - i) + "*" * (2 * i - 1))
