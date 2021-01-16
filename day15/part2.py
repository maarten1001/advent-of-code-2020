import timeit

code = """
# get the input file
f = open("input.txt")
entries = f.read()
f.close()

# https://pythonhow.com/measure-execution-time-python-code/
# https://pymotw.com/3/profile/index.html
# lookup in a set instead of iterating over the list

num = [int(x) for x in entries.split(",")]

for n in range(len(num) - 1, 20200):
    last = num[n]
    for i in range(n - 1, -1, -1):
        if num[i] == last:
            num.append(n - i)
            break
    else:
        num.append(0)
"""

elapsed_time = timeit.timeit(code, number=5)/5
print(elapsed_time)
# print(num[20200 - 1])
