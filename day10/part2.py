# get the input file
f = open("test2.txt")
numbers = f.read().splitlines()
f.close()

numbers = [int(x) for x in numbers]
numbers.sort()
numbers.insert(0, 0)  # add the outlet
numbers.append(numbers[-1] + 3)  # add the device, which is 3 higher than the highest-rated adapter

print("(" + str(numbers[0]) + ")")
for i in range(1, len(numbers) - 1):
    print(numbers[i])
print("(" + str(numbers[-1]) + ")")


def combination_count(start, end):
    for i in range(start, end):
        for j in range(i + 1, end):
            print(numbers[i:j])


combination_count(0, len(numbers))

total = 1
for i in range(len(numbers) - 2):
    if numbers[i + 2] - numbers[i] <= 3:
        print("We can choose to skip " + str(numbers[i + 1]) + ", multiplying our possible arrangements by 2")
        total *= 2

print()
print("Total amount of arrangements is " + str(total))
