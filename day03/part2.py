# get the input file
f = open("input.txt")
entries = f.read().splitlines()
f.close()

slopes = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2}
]
total = 1
for s in slopes:
    trees = 0
    pos = 0
    for row in range(0, len(entries), s["down"]):
        if entries[row][pos] == "#":
            trees += 1
        pos += s["right"]
        pos %= len(entries[0])
    print(trees)
    total *= trees

print(total)

