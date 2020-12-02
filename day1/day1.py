f = open("day1_test.txt", "r")
lst = f.readlines()
f.close()

nums = [int(l) for l in lst]
"""
d = {}

for n in nums:
    d[n] = 

for n in nums:
    try:
        s = d[2020-n]
        print((2020-n)*n)
    except:
        pass
"""
d = {}

sums = {}

for n in nums:
    for m in nums:
        if n != m: #breaks on edge case
            sums[n+m] = [n, m]

for n in nums:
    try:
        s = sums[2020-n]
        print(s[0]*s[1]*n)
    except:
        pass