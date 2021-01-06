# get the input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

time = int(lines[0])
bus = [int(x) for x in lines[1].split(",") if x != "x"]

first = [0, time]
for i in range(len(bus)):
    nextbus = bus[i] - (time % bus[i])
    if nextbus < first[1]:
        first[0] = bus[i]
        first[1] = nextbus
txt = "Next bus for line {} will arrive in {} minutes. Answer = {}"
print(txt.format(first[0], first[1], first[0] * first[1]))