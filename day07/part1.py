# get the input file
f = open("input.txt")
entries = f.read().splitlines()
f.close()

rules = dict()
bags = set()
for x in entries:
    x = x.split("s contain ")
    rules.update({x[0]: x[1]})
    if "shiny gold bag" in x[1]:
        bags.add(x[0])

while True:
    length = len(bags)
    for bag in bags.copy():
        for key, value in rules.items():
            if bag in value:
                bags.add(key)
                txt = "{} - A {}, which contains {}"
                print(txt.format(len(bags), key, value))
    if len(bags) == length:
        break
