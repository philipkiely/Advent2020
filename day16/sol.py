f = open("test.txt", "r")
t = f.read()
f.close()

tic = t.split("\n\n")

bounds = []
names = []

for ti in tic[0].split("\n"):
    names.append(ti.split(": ")[0])
    txt = ti.split(": ")[1].split(" or ")
    txt0 = txt[0].split("-")
    txt1 = txt[1].split("-")
    bounds.append([int(txt0[0]), int(txt0[1])])
    bounds.append([int(txt1[0]), int(txt1[1])])

s = 0

def in_bounds(val, bounds):
    for b in bounds:
        if b[0] <= int(v) <= b[1]:
            return True
    return False

for ti in tic[2].split("\n")[1:]:
    vals = ti.split(",")
    for v in vals:
        if not in_bounds(v, bounds):
            s += int(v)

print(s)

invalid = []

for ti in tic[2].split("\n")[1:]:
    vals = ti.split(",")
    for v in vals:
        if not in_bounds(v, bounds):
            invalid.append(ti)

valid = [ti for ti in tic[2].split("\n")[1:] if ti not in invalid]

valid = [[int(c) for c in v.split(",")] for v in valid]

cols = [[] for i in range(len(valid[0]))]


for v in valid:
    for i in range(len(v)):
        cols[i].append(v[i])

fields = [[] for i in range(len(valid[0]))]

for i in range(len(cols)):
    all_bound = []
    for j in range(0, len(bounds), 2):
        b = bounds[j]
        ob = bounds[j+1]
        bound = True
        for c in cols[i]:
            if c <= b[0] or b[1] < c < ob[0] or c >= ob[1]:
                print(b, ob, c)
                bound = False
        all_bound.append(bound)
    for k in range(len(all_bound)):
        if all_bound[k]:
            fields[i].append(k)

print(fields)

used = [-1 for i in range(len(valid[0]))]

while -1 in used:
    for d in range(len(fields)):
        ld = fields[d]
        if len(ld) == 1:
            used[d] = ld[0]
        else:
            for u in used:
                if u in ld:
                    ld.remove(u)

print(used)

my_tic = [int(q) for q in tic[1].split("\n")[1].split(",")]

m = 1

for u in range(len(used)):
    if "departure" in names[u]:
        print(my_tic[used.index(u)])
        m *= my_tic[used.index(u)]

print(m)

# 1952671648819
# 2766491048287
