# get the input file
f = open("input.txt")
entries = f.read()
f.close()

entries = entries.split("\n\n")

total = 0
for x in entries:
    x = x.replace("\n", "")
    answers = set(x)
    print(len(answers))
    total += len(answers)

print(total)
