# get the input file
f = open("input.txt")
entries = f.read()
f.close()

num = [int(x) for x in entries.split(",")]

for n in range(len(num) - 1, 2020):
    last = num[n]
    for i in range(n - 1, -1, -1):
        if num[i] == last:
            num.append(n - i)
            break
    else:
        num.append(0)

print(num[2020 - 1])
