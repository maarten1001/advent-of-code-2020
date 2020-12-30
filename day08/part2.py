# get the input file
f = open("input.txt")
entries = f.read().splitlines()
f.close()

for fix in range(len(entries)):
    acc = 0
    i = 0
    executed = [False for x in range(len(entries))]
    print("Fixing line " + str(fix + 1))
    while True:
        if i == len(entries):
            print("Achieved termination by changing the instruction in line " + str(fix + 1))
            print("Accumulator value is " + str(acc))
            quit(0)
        elif executed[i]:
            print("Attempting to execute the instruction in line " + str(i + 1) + " for the second time")
            print("")
            break
        else:
            executed[i] = True
            instr = entries[i].split()
            # print(str(i + 1) + ": " + str(instr))
            op = instr[0]
            arg = instr[1]
            if op == "acc":
                acc += int(arg)
                i += 1
            elif (op == "jmp" and fix != i) or (op == "nop" and fix == i):
                i += int(arg)
            elif (op == "nop" and fix != i) or (op == "jmp" and fix == i):
                i += 1
            else:
                print("invalid operation" + op)
