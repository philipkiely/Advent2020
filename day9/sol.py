f = open("test.txt", "r")
nums = [int(c) for c in f.readlines()]
f.close()

len_preamble = 25

vals = {}

for i in range(len_preamble):
    vals[nums[i]] = 0

def is_sum(v, n):
    for a in v:
        if n-a in v and n-a != a:
            return -1
    print(n)
    return n

x = -1

for i in range(len(nums) - len_preamble):
    j = i + len_preamble
    x = is_sum(vals, nums[j])
    if x != -1:
        break
    del vals[nums[i]]
    vals[nums[j]] = 0


def crack(nums, x):
    con = []
    s = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            con.append(nums[i+j])
            s += nums[i+j]
            if s == x:
                print(min(con) + max(con))
                return
            elif s > x:
                con = []
                s = 0
                break

crack(nums, x)