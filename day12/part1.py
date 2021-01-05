# get the input file
f = open("input.txt")
instr = f.read().splitlines()
f.close()

x = 0
y = 0
facing = 90  # east

for i in instr:
    if i[0] == "N":
        y += int(i[1:])
    elif i[0] == "S":
        y -= int(i[1:])
    elif i[0] == "E":
        x += int(i[1:])
    elif i[0] == "W":
        x -= int(i[1:])
    elif i[0] == "L":
        facing = (facing - int(i[1:])) % 360
    elif i[0] == "R":
        facing = (facing + int(i[1:])) % 360
    elif i[0] == "F":
        if facing == 0:
            y += int(i[1:])
        elif facing == 90:
            x += int(i[1:])
        elif facing == 180:
            y -= int(i[1:])
        elif facing == 270:
            x -= int(i[1:])
        else:
            print("Facing direction " + str(facing) + " is invalid")
    else:
        print("Instruction " + i + " is invalid")
    txt = "Position: {}, {} facing {}"
    print(txt.format(x, y, facing))

print()
print("Manhattan distance is " + str(abs(x) + abs(y)))
