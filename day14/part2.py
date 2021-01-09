# get the input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

mask = ""
mem = dict()


def apply_mask(string):
    string = format(int(string), '036b')
    for i in range(len(mask)):
        if mask[i] == "0":
            continue
        string = string[:i] + mask[i] + string[i + 1:]
    return string


def write_to_memory(addr, value, bit=0):
    for i in range(bit, len(addr)):
        if addr[i] == "X":
            write_to_memory(addr[:i] + "0" + addr[i + 1:], value, i + 1)
            write_to_memory(addr[:i] + "1" + addr[i + 1:], value, i + 1)
            return
    mem[int(addr, 2)] = int(value)


for line in lines:
    line = line.split(" = ")
    if line[0] == "mask":
        mask = line[1]
    else:
        address = apply_mask(line[0][4:-1])
        write_to_memory(address, line[1])

print(sum(mem.values()))
