f = open("test.txt", "r")
m = f.readlines()
f.close()

# part 1 answer is buried in here basically

big_count = 1

m = [l.replace("\n", "")*700 for l in m]

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

for s in slopes:
    x = 0
    y = 0
    count = 0
    while y < (len(m)-1):
        x += s[0]
        y += s[1]
        if m[y][x] == "#":
            count += 1
    big_count *= count

print(big_count)