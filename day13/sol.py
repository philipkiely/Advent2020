f = open("test.txt", "r")
sched = f.readlines()
f.close()

t = int(sched[0].strip())

lines = [int(x) for x in sched[1].split(",") if x != "x"]

m = t
n = -1

for l in lines:
    w = l - (t % l)
    if w < m:
        m = w
        n = l

print(t, m, n)

print(n * m)

lines = [int(x) if x != "x" else 1 for x in sched[1].split(",")]

time = lines[0]
inc = lines[0]
i = 1

times = []

while i < len(lines):
    #print(time, i, lines[i], inc)
    if (time + i) % lines[i] == 0:
        inc *= lines[i]
        i += 1
    times.append(time)
    time += inc

print(time - inc)


def check(time, lines):
    for i in range(len(lines)):
        if (time + i) % lines[i] != 0:
            return False
    return True

for t in times:
    if check(t, lines):
        print(t)
        break
"""
lines = [int(x) if x != "x" else 1 for x in sched[1].split(",")]


def check(time, lines):
    for i in range(len(lines)):
        if (time + i) % lines[i] != 0:
            return False
    return True

#j = 99999999999972  # largest multiple of lines[0] < 100000000000000
j = lines[0]
sol = False
while not sol:
    j += lines[0]
    sol = check(j, lines)

#print(j)
#print(j)


lines = [int(x) if x != "x" else 1 for x in sched[1].split(",")]

count = 0

active = {}

for l in lines:
    if l != 1:
        active[l] = count
    count += 1

#print(active)

def faster_check(time, active):
    for a in active: # order is unofficially guaranteed in dicts in python >= 3.6 but this is not a good pracice for production code
        if (time + active[a]) % a != 0:
            return False
    return True


j = lines[0]
#j = 99999999999972  # largest multiple of lines[0] < 100000000000000

sol = False
while not sol:
    j += lines[0]
    sol = faster_check(j, active)

#print(active)
#print(j)

active = {17: 0, 13: 2, 19: 3}


j = 0
#j = 99999999999972  # largest multiple of lines[0] < 100000000000000

sol = False
while not sol:
    j += 17
    sol = faster_check(j, active)

#print(active)
#print(j)

active = {29: 0, 37: 23, 467: 29, 23: 37, 13: 42, 17: 46, 19: 48, 443: 60, 41: 101}

b = 1

for a in active:
    b *= a

#print(b)
"""

"""
active = {}
count = 0

for l in lines:
    if l != 1:
        active[l] = count
        count = 0
    count += 1

#print(active)

s = 1

for a in active:
    s *= (a - active[a])

#print(s)

s2 = 0

for a in active:
    s2 += active[a]

#print("Answer:", s + lines[0]*s2)
"""

