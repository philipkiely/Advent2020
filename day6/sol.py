import math

f = open("test.txt", "r")
d = f.read()
f.close()

groups = d.split("\n\n")

count = 0

"""
for g in groups:
    chars = [0]*26
    for c in g:
        if c != "\n":
            chars[ord(c)-97] = 1
    count += sum(chars)
"""

for g in groups:
    chars = []
    ans = g.split("\n")
    for a in ans:
        chars.append([0]*26)
        for c in a:
            if c != "\n":
                chars[-1][ord(c)-97] = 1
    fin = [0]*26
    for i in range(26):
        for c in chars:
            fin[i] += c[i]
        fin[i] = math.floor(fin[i]/len(ans))
    count += sum(fin)

print(count)