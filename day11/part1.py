# get the input file
f = open("input.txt")
seats = f.read().splitlines()
f.close()

# add padding
padding = "." * len(seats[0])
seats.insert(0, padding)
seats.append(padding)
for i in range(len(seats)):
    seats[i] = "." + seats[i] + "."


def print_seats(r):
    occupied = 0
    print("Round " + str(r) + ":")
    for ii in range(1, len(seats) - 1):
        print(seats[ii][1:-1])
        occupied += seats[ii].count("#")
    print()
    print(str(occupied) + " seats are occupied")
    print()


def count_adjacent(x, y):
    total = 0
    total += seats[x - 1][y - 1] == "#"
    total += seats[x - 1][y] == "#"
    total += seats[x - 1][y + 1] == "#"
    total += seats[x][y - 1] == "#"
    total += seats[x][y + 1] == "#"
    total += seats[x + 1][y - 1] == "#"
    total += seats[x + 1][y] == "#"
    total += seats[x + 1][y + 1] == "#"
    return total


rounds = 0
print_seats(rounds)

while True:
    rounds += 1
    changed = False
    s2 = seats.copy()
    for i in range(len(s2)):
        for j in range(len(s2[i])):
            if seats[i][j] == "L" and count_adjacent(i, j) == 0:
                s2[i] = s2[i][:j] + "#" + s2[i][j + 1:]
                changed = True
            elif seats[i][j] == "#":
                if count_adjacent(i, j) >= 4:
                    s2[i] = s2[i][:j] + "L" + s2[i][j + 1:]
                    changed = True
    if changed:
        seats = s2
        print_seats(rounds)
    else:
        break
