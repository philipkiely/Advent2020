f = open("test.txt", "r")
jolts = [int(n) for n in f.readlines()]
f.close()

jolts.sort()

jolts = [0] + jolts

jolts.append(jolts[-1] + 3)

one_gap = 0
three_gap = 0

for i in range(len(jolts)-1):
    diff = jolts[i+1] - jolts[i]
    if diff == 1:
        one_gap += 1
    elif diff == 3:
        three_gap += 1

print(one_gap * three_gap)

s = [0, 0, 0, 0, 0]

def traverse(lst, i):
    global s
    if len(lst) == 1:
        s[i] += 1
        return
    if lst[0] + 3 >= lst[1]:
        traverse(lst[1:], i)
    if len(lst) >= 3:
        if lst[0] + 3 >= lst[2]:
            traverse(lst[2:], i)
    if len(lst) >= 4:
        if lst[0] + 3 >= lst[3]:
            traverse(lst[3:], i)

print(jolts[40:60])

#traverse(jolts[:15], 0)
#traverse(jolts[15:], 1)
traverse(jolts[:51], 0)
traverse(jolts[51:], 1) # Gap MUST be 3
#traverse(jolts[40:60], 2)
#traverse(jolts[60:80], 3)
#traverse(jolts[80:], 4)

print(s[0]*s[1])#*s[2]*s[3]*s[4])