# get the input file
f = open("input.txt")
entries = f.read()
f.close()

entries = entries.split("\n\n")

# we don't check cid
fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
valid = 0

for x in entries:
    passport = {}
    for field in x.split():
        part = field.split(":")
        passport[part[0]] = part[1]
    print(passport)
    for y in fields:
        if y not in passport:
            print("invalid")
            break
    else:
        print("valid")
        valid += 1
    print(" ")

print(valid)
