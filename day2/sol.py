f = open("test.txt", "r")
lst = f.readlines()
f.close()

passwords = []

for l in lst:
    c = l.split(" ")
    e = {}
    e["min"] = int(c[0].split("-")[0])
    e["max"] = int(c[0].split("-")[1])
    e["letter"] = c[1][0]
    e["word"] = c[2]
    passwords.append(e)

valid = 0

"""
for p in passwords:
    count = 0
    for c in p["word"]:
        if c == p["letter"]:
            count += 1
    if p["min"] <= count <= p["max"]:
        valid += 1
"""

for p in passwords:
    if (p["word"][p["min"]-1] == p["letter"] and p["word"][p["max"]-1] != p["letter"]) or (p["word"][p["min"]-1] != p["letter"] and p["word"][p["max"]-1] == p["letter"]):
        valid += 1

print(valid)