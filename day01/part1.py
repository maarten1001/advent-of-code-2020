# get the input numbers
f = open("input.txt")
entries = f.read().splitlines()
f.close()

#https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
entries = list(map(int, entries))

for x in range(len(entries) - 1):
    for y in range(x + 1,len(entries)):
        if entries[x] + entries[y] == 2020:
            print(entries[x] * entries[y])
            quit(0)

