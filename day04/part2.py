import re

# get the input file
f = open("input.txt")
entries = f.read()
f.close()


def validate_passport(p):
    for y in fields:
        if y not in p:
            print("missing field " + y)
            return False
    if re.match(r"^\d{4}$", p["byr"]) is None or int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
        print("invalid byr")
        return False
    elif re.match(r"^\d{4}$", p["iyr"]) is None or int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
        print("invalid iyr")
        return False
    elif re.match(r"^\d{4}$", p["eyr"]) is None or int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
        print("invalid eyr")
        return False
    elif re.match(r"^#[0-9a-f]{6}$", p["hcl"]) is None:
        print("invalid hcl")
        return False
    elif p["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        print("invalid ecl")
        return False
    elif re.match(r"^\d{9}$", p["pid"]) is None:
        print("invalid pid")
        return False
    else:
        hgt = re.match(r"^(\d{2,3})(cm|in)$", p["hgt"])
        if hgt is None:
            print("invalid hgt")
            return False
        else:
            if hgt.group(2) == "cm" and (int(hgt.group(1)) < 150 or int(hgt.group(1)) > 193):
                print("invalid - " + hgt.group(0))
                return False
            elif hgt.group(2) == "in" and (int(hgt.group(1)) < 59 or int(hgt.group(1)) > 76):
                print("invalid - " + hgt.group(0))
                return False
            else:
                print("valid")
                return True


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
    if validate_passport(passport):
        valid += 1
    print(" ")


print(valid)
