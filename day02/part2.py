# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

valid = 0

for x in entries:
    list1 = x.split()
    bounds = list1[0].split("-")
    bounds = list(map(int, bounds))
    char = list1[1][0]
    password = list1[2]

#   if (password[bounds[0] - 1] == char and password[bounds[1] - 1] != char) or (password[bounds[0] - 1] != char and password[bounds[1] - 1] == char):
#       valid += 1
    if (password[bounds[0] - 1] == char) ^ (password[bounds[1] - 1] == char) == 1:
        valid += 1
print(valid)

