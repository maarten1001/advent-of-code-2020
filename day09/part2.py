# get the input file
f = open("input.txt")
numbers = f.read().splitlines()
f.close()

preamble = 25
target = 248131121
numbers = [int(x) for x in numbers]

for x in range(len(numbers)):
    for y in range(x + 1, len(numbers)):
        if sum(numbers[x:y + 1]) == target:
            txt = "{} is the sum of the numbers from {} to {}"
            print(txt.format(target, numbers[x], numbers[y]))
            small = min(numbers[x:y + 1])
            large = max(numbers[x:y + 1])
            txt = "The smallest number is {}, the largest number is {}. Their sum is {}"
            print(txt.format(small, large, small + large))
