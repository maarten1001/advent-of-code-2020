# get the input file
f = open("input.txt")
instr = f.read().splitlines()
f.close()


class Ship:
    def __init__(self, coords, waypoint):
        self.x = coords[0]
        self.y = coords[1]
        self.wx = waypoint[0]
        self.wy = waypoint[1]

    def move(self, x, y):
        self.wx += x
        self.wy += y

    def move_to_waypoint(self, n):
        self.x += self.wx * n
        self.y += self.wy * n

    def rotate_right(self, degrees):
        if degrees == 90 or degrees == 270:
            temp = self.wy
            self.wy = -self.wx
            self.wx = temp
        if degrees == 180 or degrees == 270:
            self.wx = -self.wx
            self.wy = -self.wy

    def print_location(self):
        txt = "Ship: {}, {} Waypoint: {}, {}"
        print(txt.format(self.x, self.y, self.wx, self.wy))


ship = Ship((0, 0), (10, 1))
for i in instr:
    if i[0] == "N":
        ship.move(0, int(i[1:]))
    elif i[0] == "S":
        ship.move(0, -int(i[1:]))
    elif i[0] == "E":
        ship.move(int(i[1:]), 0)
    elif i[0] == "W":
        ship.move(-int(i[1:]), 0)
    elif i[0] == "L":
        ship.rotate_right(360 - int(i[1:]))
    elif i[0] == "R":
        ship.rotate_right(int(i[1:]))
    elif i[0] == "F":
        ship.move_to_waypoint(int(i[1:]))
    else:
        print("Instruction " + i + " is invalid")
    ship.print_location()

print()
print("Manhattan distance is " + str(abs(ship.x) + abs(ship.y)))
