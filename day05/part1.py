# get the input file
f = open("input.txt")
entries = f.read().splitlines()
f.close()

maxid = 0
for x in entries:
    # replace F or L with 0 and B or R with 1
    mytable = x.maketrans("FBLR", "0101")
    binary = x.translate(mytable)
    row = int(binary[:-3], 2)
    column = int(binary[-3:], 2)
    seatid = int(binary, 2)
    txt = "{}: row {}, column {}, seat ID {}."
    print(txt.format(x, row, column, seatid))
    if seatid > maxid:
        maxid = seatid

print(maxid)
