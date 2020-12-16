f = open("test.txt", "r")
starting = [int(x) for x in f.read().split(",")]
f.close()

turn = 0
cur_spoken = {}
prev_spoken = {}
cur = -1
prev = -1

for s in starting:
    turn += 1
    prev = cur
    cur = s
    prev_spoken[prev] = turn-1
    cur_spoken[cur] = turn

while turn <= 30000000:
    turn += 1
    if cur not in prev_spoken:
        prev = cur
        cur = 0
    else:
        prev = cur
        cur = turn - prev_spoken[cur] - 1
    prev_spoken[prev] = turn-1
    cur_spoken[cur] = turn

print(prev)
