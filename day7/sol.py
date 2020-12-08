f = open("test.txt", "r")
bags = f.readlines()
f.close()

all_colors = [b.split(" bags ")[0] for b in bags]

num_bags = len(bags)

all_colors_lookup = {}
for i in range(len(all_colors)):
    all_colors_lookup[all_colors[i]] = i

matches = []

for b in bags:
    a = b.split(" contain ")
    cur = a[0][:-5]
    m = [0] * num_bags
    if "no " not in a[1]:
        if "," in a[1]:
            v = a[1].split(", ")
            for c in v:
                c = c.split(" ")
                num = int(c[0])
                color = " ".join(c[1:3])
                m[all_colors_lookup[color]] = num
        else:
            v = a[1].split(" ")
            num = int(v[0])
            color = " ".join(v[1:3])
            m[all_colors_lookup[color]] = num
    matches.append(m)



dex = all_colors_lookup["shiny gold"]
"""
# Doesn't work, bad approach
contains_sg = 0
containers = set()

def find_cont(j, c, contains_sg):
    containers = set()
    for i in range(num_bags):
        if matches[i][j] > 0 and i not in c:
            containers.add(i)
            matches[i][j] = 0
    contains_sg += len(containers)
    return containers, contains_sg

containers, contains_sg = find_cont(dex, containers, contains_sg)

while len(containers) > 0:
    containers_old = containers
    containers_new = set()
    for m in containers_old:
        tmp, contains_sg = find_cont(m, containers_new, contains_sg)
        for t in tmp:
            containers_new.add(t)
    containers = containers_new
"""

def explorer(row, m):
    if m == dex:
        return 1
    elif matches[row][m] > 0:
        return explore(m)
    else:
        return 0

def explore(row):
    if sum([explorer(row, m) for m in range(num_bags) if matches[row][m] > 0]) > 0:
        return 1
    return 0

print(sum([explore(m) for m in range(num_bags)]))

def explorer_up(row, m):
    if m == dex:
        return matches[m][row]
    elif matches[m][row] > 0:
        return matches[m][row] * explore_up(m)
    else:
        return 0

def explore_up(row):
    return sum([explorer_up(row, m) for m in range(num_bags) if matches[m][row] > 0])

print(sum([explore_up(m) for m in range(num_bags)]))