# import cProfile

# get the input file
f = open("input.txt")
entries = f.read()
f.close()

# set up a dict where each value is the last index of its key
num = [int(x) for x in entries.split(",")]
index_of = dict()
for ii in range(0, len(num) - 1):
    index_of.update({num[ii]: ii})


def next_number(limit):
    start = len(num) - 1
    last = num[start]
    for n in range(start, limit - 1):
        if last not in index_of:
            index_of[last] = n
            last = 0
        else:
            diff = n - index_of[last]
            index_of[last] = n
            last = diff
    print(last)


next_number(30000000)

# cProfile.run('next_number(30000000); print()')

# traversing the list backwards to find the offset to the previous index
# range     2020 -    20203 function calls in   4.359 seconds
# range    20200 -   202003 function calls in 404.016 seconds

# using a set lookup before traversal to check if the number was seen before
# to prevent traversal of the entire list
# range     2020 -     2403 function calls in   0.062 seconds
# range    20200 -    23520 function calls in   1.438 seconds
# range   300000 -   343093 function calls in 224.312 seconds
# still too slow

# using a dict to store the previous index of all numbers
# range     2020 -     2023 function calls in   0.016 seconds
# range    20200 -    20203 function calls in   0.094 seconds
# range   300000 -   300003 function calls in   1.219 seconds
# range 30000000 - 30000003 function calls in 120.266 seconds

# solution = 47205

# no longer expanding the list
# range     2020 -        8 function calls in   0.016 seconds
# range    20200 -        8 function calls in   0.031 seconds
# range   300000 -        8 function calls in   0.109 seconds
# range 30000000 -        8 function calls in  14.469 seconds
