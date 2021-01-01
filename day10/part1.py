# get the input file
f = open("input.txt")
numbers = f.read().splitlines()
f.close()

numbers = [int(x) for x in numbers]
numbers.sort()
numbers.insert(0, 0)  # add the outlet

jolt = dict()
jolt[1] = 0
jolt[3] = 1  # last adapter to the device
for x in range(len(numbers) - 1):
    diff = numbers[x + 1] - numbers[x]
    jolt[diff] += 1

txt = "In this example there are {} differences of 1 jolt and {} differences of 3 jolts."
print(txt.format(jolt[1], jolt[3]))
txt = "{} * {} = {}"
print(txt.format(jolt[1], jolt[3], jolt[1] * jolt[3]))
