import re

# get the input file
f = open("input.txt")
lines = f.read()
f.close()

lines = lines.split("\n\n")
rules = lines[0].split("\n")
ticket = lines[1].split("\n")[1]
ticket = [int(x) for x in ticket.split(",")]
nearby = lines[2].split("\n")[1:]
for i in range(len(nearby)):
    nearby[i] = [int(x) for x in nearby[i].split(",")]

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
    for value in t:
        if value not in valid:
            error_rate += value
            nearby.remove(t)
            break

possible_fields = [list(fields.keys()) for x in fields]

# determine the order of the fields
while True:
    changed = False
    for t in nearby:
        for i in range(len(t)):
            for key, values in fields.items():
                if t[i] not in values:
                    if key in possible_fields[i]:
                        possible_fields[i].remove(key)
                    # if a field has been identified, remove that option from the other fields
                    if len(possible_fields[i]) == 1:
                        unique_field = possible_fields[i][0]
                        for p in possible_fields:
                            if len(p) > 1 and unique_field in p:
                                p.remove(unique_field)
                                changed = True
    if not changed:
        break

product = 1
for i in range(len(possible_fields)):
    if "departure" in possible_fields[i][0]:
        product *= int(ticket[i])
    print(str(i + 1) + " - " + str(possible_fields[i]))
print()
print(product)
