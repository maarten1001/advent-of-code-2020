# get the input file
f = open("input.txt")
entries = f.read()
f.close()

entries = entries.split("\n\n")

total = 0
for i, x in enumerate(entries):
    group = x.split()
    group = [set(x) for x in group]
    for char in group[0]:
        # check if char is in the answers from other people in the group too
        for j in range(1, len(group)):
            if char not in group[j]:
                break
        else:
            total += 1
            print("found answer " + char + " for everyone in group " + str(i + 1))

print("")
print("total = " + str(total))
