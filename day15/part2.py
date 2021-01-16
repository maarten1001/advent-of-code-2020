# import timeit
import profile

# get the input file
f = open("input.txt")
entries = f.read()
f.close()

num = [int(x) for x in entries.split(",")]
unique_num = set(num[:-1])


def next_number():
    for n in range(len(num) - 1, 300000):
        # print(num)
        # print(unique_num)
        last = num[n]
        # print("Last number is " + str(last))
        # lookup in a set instead of iterating over the list
        if last not in unique_num:
            # print("Not seen before, append 0")
            num.append(0)
            # print("Add " + str(last) + " to the set")
            unique_num.add(last)
        else:
            for i in range(n - 1, -1, -1):
                if num[i] == last:
                    # print("Seen before, append " + str(n-i))
                    num.append(n - i)
                    break


profile.run('next_number(); print(num[300000 - 1]); print(unique_num); print()')

# before set lookup
# range   2020 -  20203 function calls in   4.359 seconds
# range  20200 - 202003 function calls in 404.016 seconds

# after set lookup
# range   2020 -   2403 function calls in   0.062 seconds
# range  20200 -  23520 function calls in   1.438 seconds
# range 300000 - 343093 function calls in 224.312 seconds
# still too slow
