# get the input file
f = open("input.txt")
numbers = f.read().splitlines()
f.close()

preamble = 25
numbers = [int(x) for x in numbers]

for i in range(preamble + 1, len(numbers)):
    valid = False
    for x in range(i - preamble, i):
        for y in range(x + 1, i):
            if numbers[x] + numbers[y] == numbers[i]:
                # found the sum
                valid = True
                break
    if not valid:
        txt = "{} is not a sum of the previous {} numbers"
        print(txt.format(numbers[i], preamble))
