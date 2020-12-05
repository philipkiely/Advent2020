import math

f = open("test.txt", "r")
boarding_passes = f.readlines()
f.close()

def find_id(row, col):
    return (row * 8) + col

def adjust_bounds(lo, hi, d):
    if d == "B" or d == "R":
        return lo + math.ceil((hi-lo)/2), hi
    else:
        return lo, hi - math.ceil((hi-lo)/2)

def find_row(s):
    lo = 0
    hi = 127
    for c in s:
        lo, hi = adjust_bounds(lo, hi, c)
    return lo

def find_col(s):
    lo = 0
    hi = 7
    for c in s:
        lo, hi = adjust_bounds(lo, hi, c)
    return hi


def find_seat(bp):
    row = find_row(bp[:7])
    col = find_col(bp[7:])
    return find_id(row, col)

# print(max([find_seat(bp) for bp in boarding_passes]))

seats = [find_seat(bp) for bp in boarding_passes]

seats.sort()

for i in range(len(seats)):
    if seats[i] != seats[i+1] - 1:
        print(seats[i], seats[i+1])
        # yes this triggers an index out of range error but it gives the answer first