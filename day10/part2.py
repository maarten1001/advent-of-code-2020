# get the input file
f = open("input.txt")
adapters = f.read().splitlines()
f.close()

adapters = [int(x) for x in adapters]
adapters.sort()
adapters.insert(0, 0)  # add the outlet
adapters.append(adapters[-1] + 3)  # add the device, which is 3 higher than the highest-rated adapter

# count the number of arrangements from 0 to adapter n
total = [0 if x != 0 else 1 for x in range(max(adapters) + 1)]

for ad in adapters:
    # add the possible arrangements from the previous 3 adapters
    for i in range(ad - 3, ad):
        if i < 0:
            continue
        total[ad] += total[i]

print()
print("Total amount of arrangements is " + str(total[-1]))
