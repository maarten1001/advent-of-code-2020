import re

# get the input file
f = open("input.txt")
entries = f.read()
f.close()

entries = entries.split("\n\n")
rules = entries[0]
ticket = entries[1].split("\n")[1]
nearby = entries[2].split("\n")[1:]

# process the rules into a set of valid values
valid = set()
reg_rule = re.findall(r"([0-9]+)-([0-9]+)", rules)
for rule in reg_rule:
    for i in range(int(rule[0]), int(rule[1]) + 1):
        valid.add(i)

error_rate = 0
for t in nearby:
    values = [int(x) for x in t.split(",")]
    for v in values:
        if v not in valid:
            error_rate += v

print(error_rate)
