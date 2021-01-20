import re

# get the input file
f = open("test.txt")
lines = f.read()
f.close()

lines = lines.split("\n\n")
rules = lines[0].split("\n")
ticket = lines[1].split("\n")[1]
nearby = lines[2].split("\n")[1:]

# process the rules into a set of fields and valid values
valid = set()
fields = dict()
for rule in rules:
    name = rule[:rule.index(":")]
    fields[name] = set()
    reg_rule = re.findall(r"([0-9]+)-([0-9]+)", rule)
    for r in reg_rule:
        for i in range(int(r[0]), int(r[1]) + 1):
            valid.add(i)
            fields[name].add(i)

error_rate = 0
# discard invalid tickets
# https://sopython.com/canon/95/removing-items-from-a-list-while-iterating-over-the-list/
for t in nearby.copy():
    values = [int(x) for x in t.split(",")]
    for v in values:
        if v not in valid:
            error_rate += v
            nearby.remove(t)
            break

# determine the order of the fields
possible_fields = [set(fields.keys()) for x in fields]
print(possible_fields)

print("The error rate is " + str(error_rate))
print()
print("Valid tickets:")
print(nearby)
