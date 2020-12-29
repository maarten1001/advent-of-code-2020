import re

# get the input file
f = open("input.txt")
entries = f.read().splitlines()
f.close()

rules = dict()
for x in entries:
    x = x.split(" contain ")
    rules.update({x[0]: x[1]})

print(rules)


def bags_in(container):
    if "no other bags" in rules[container]:
        return 1
    else:
        total = 1
        bags = re.findall(r"([0-9]) ([a-z ]+)", rules[container])
        for bag in bags:
            amount = bag[0]
            key = bag[1]
            # add final "s" if necessary
            if key[-1] != "s":
                key = key + "s"
            total += (int(amount) * bags_in(key))
            text = "{} contain {} {}"
            print(text.format(container, amount, key))
        return total


totalbags = bags_in("shiny gold bags")
txt = "1 shiny gold bag contains {} other bags"
print("")
print(txt.format(totalbags - 1))
