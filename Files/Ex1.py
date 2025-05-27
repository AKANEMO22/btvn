x = input("Enter a file name: ")
with open(x, 'r') as fhand:
    for line in fhand:
        print(line.upper().strip())
