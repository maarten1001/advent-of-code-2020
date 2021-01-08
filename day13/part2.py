# get the input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

bus = [x for x in lines[1].split(",")]


def gcd(a, b):
    """Return the Greatest Common Divisor of a and b, using Euclid's algorithm"""
    while b != 0:
        tt = b
        b = a % b
        a = tt
    return a


def lcm(a, b):
    """Return the Lowest Common Multiple of a and b"""
    return abs(a * b) // gcd(a, b)


t = 0
step = 1

for i in range(len(bus)):
    if bus[i] == "x":
        continue
    while (t + i) % int(bus[i]) != 0:  # bus[i] does not depart at time t + i
        t += step
    else:
        step = lcm(step, int(bus[i]))  # increase the step size

print("t = " + str(t))
