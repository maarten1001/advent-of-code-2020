# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

valid = 0

for x in entries:
    list = x.split()
    bounds = list[0].split("-")
    char = list[1][0]
    password = list[2]
    if password.count(char) >= int(bounds[0]) and password.count(char) <= int(bounds[1]):
        valid += 1
print(valid)
