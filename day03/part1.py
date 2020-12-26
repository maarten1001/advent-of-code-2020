# get the input file
f = open("input.txt")
entries = f.read().splitlines()
f.close()

trees = 0
x = 0
for row in entries:
    if row[x] == "#":
        trees += 1
        #https://pythonexamples.org/python-string-replace-character-at-specific-position/
        row = row[:x] + "X" + row[x+1:]
    else:
        row = row[:x] + "O" + row[x+1:]
    print(row)
    x += 3
    x %= len(entries[0])

print(trees)
