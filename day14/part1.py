# get the input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

mask = ""
mem = dict()


def apply_mask(string):
    string = format(int(string), '036b')
    for i in range(len(mask)):
        if mask[i] == "X":
            continue
        string = string[:i] + mask[i] + string[i + 1:]
    return int(string, 2)


for line in lines:
    line = line.split(" = ")
    if line[0] == "mask":
        mask = line[1]
    else:
        address = line[0][4:-1]
        mem[address] = apply_mask(line[1])

print(sum(mem.values()))
