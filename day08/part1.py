# get the input file
f = open("input.txt")
entries = f.read().splitlines()
f.close()

acc = 0
i = 0
executed = [False for x in range(len(entries))]

while True:
    if executed[i]:
        print(acc)
        break
    else:
        executed[i] = True
        instr = entries[i].split()
        print(instr)
        op = instr[0]
        arg = instr[1]
        if op == "acc":
            acc += int(arg)
            i += 1
        elif op == "jmp":
            i += int(arg)
        elif op == "nop":
            i += 1
        else:
            print("invalid operation" + op)
