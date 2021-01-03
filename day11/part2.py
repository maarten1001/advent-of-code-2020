# get the input file
f = open("input.txt")
seats = f.read().splitlines()
f.close()


def print_seats(r):
    occupied = 0
    print("Round " + str(r) + ":")
    for i in range(len(seats)):
        print(seats[i])
        occupied += seats[i].count("#")
    print()
    print(str(occupied) + " seats are occupied")
    print()


def seat_in_direction(x, y, direction):
    while True:
        x += direction[0]
        y += direction[1]
        if x < 0 or x >= len(seats[0]) or y < 0 or y >= len(seats):
            return 0
        if seats[y][x] == "#":
            # print("Occupied seat at " + str(x + 1) + ", " + str(y + 1))
            return 1
        if seats[y][x] == "L":
            # print("Empty seat at " + str(x + 1) + ", " + str(y + 1))
            return 0


def count_adjacent(y, x):
    total = 0
    total += seat_in_direction(x, y, (-1, -1))
    total += seat_in_direction(x, y, (0, -1))
    total += seat_in_direction(x, y, (1, -1))
    total += seat_in_direction(x, y, (-1, 0))
    total += seat_in_direction(x, y, (1, 0))
    total += seat_in_direction(x, y, (-1, 1))
    total += seat_in_direction(x, y, (0, 1))
    total += seat_in_direction(x, y, (1, 1))
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
            elif seats[i][j] == "#" and count_adjacent(i, j) >= 5:
                s2[i] = s2[i][:j] + "L" + s2[i][j + 1:]
                changed = True
    if changed:
        seats = s2
        print_seats(rounds)
    else:
        break
