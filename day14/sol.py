import math

# Herein I make a mockery of computing by using a large number
# of relatively expensive data stuctures and algorithms to emulate
# extremely efficient bitwise operations and direct memory accesses

f = open("test.txt", "r")
ins = [x.strip("\n") for x in f.readlines()]
f.close()

def nearest_lesser_eq_power(n, p):
    i = 0
    if p < 2:
        return math.inf # not sure if this is mathematically true but better than an error or infinite loop
    while True:
        if p**i <= n < p**(i+1):
            return p**i
        i += 1

def power_of(n, p): # precondition: n is a power of p
    i = 0
    while n > 1:
        n = n / p
        i += 1
    return i

def int_to_bits(n):
    bits = {}
    while n > 0:
        b = nearest_lesser_eq_power(n, 2)
        bits[power_of(b, 2)] = 1
        n = n - b
    return bits

def bits_to_int(bits):
    n = 0
    for b in bits:
        n += 2**b
    return n

def mask_bits(bits, mask):
    mask = mask[::-1]
    for i in range(len(mask)):
        if mask[i] == "1":
            bits[i] = 1
        elif mask[i] == "0" and i in bits:
            del bits[i]
    return bits

def enumerate_floating(bits):
    enum = []
    exed = False
    for b in bits:
        if bits[b] == "X":
            exed = True
            copy = {}
            for bi in bits:
                copy[bi] = bits[bi]
            copy[b] = 1
            enum += enumerate_floating(copy)
            del copy[b]
            enum += enumerate_floating(copy)
    if not exed:
        return [bits]
    return enum

def floating_mask_bits(bits, mask):
    mask = mask[::-1]
    for i in range(len(mask)):
        if mask[i] == "1":
            bits[i] = 1
        elif mask[i] == "X":
            bits[i] = "X"
    most = enumerate_floating(bits)
    for b in bits:
        if bits[b] == "X":
            bits[b] = 1
    return most + [bits]


mem = {}
mask = ""

for line in ins:
    line = line.split(" = ")
    if line[0] == "mask":
        mask = line[1]
    else:
        mem_index = int(line[0][4:-1])
        val = int(line[1])
        mem[mem_index] = bits_to_int(mask_bits(int_to_bits(val), mask))

s = 0
for m in mem:
    s += mem[m]

print(s)
"""
mem = {}
mask = ""

for line in ins:
    print(line)
    line = line.split(" = ")
    if line[0] == "mask":
        mask = line[1]
    else:
        mem_index = int(line[0][4:-1])
        val = int(line[1])
        dexes = list(set(bits_to_int(d) for d in floating_mask_bits(int_to_bits(mem_index), mask)))
        for d in dexes:
            mem[d] = val

s = 0
for m in mem:
    s += mem[m]

print(s)
"""

def afm_helper(num, mask, i, val):
    global dexes
    if i == len(mask):
        dexes.append(val)
        return
    if mask[i] == "0":
        if num == num | 2**i:
            return afm_helper(num, mask, i+1, val + 2**i)
        return afm_helper(num, mask, i+1, val)
    if mask[i] == "1":
        afm_helper(num, mask, i+1, val + 2**i)
    if mask[i] == "X":
        up = afm_helper(num, mask, i+1, val+2**i)
        down = afm_helper(num, mask, i+1, val)

def apply_floating_mask(num, mask):
    mask = mask[::-1]
    afm_helper(num, mask, 0, 0)


mem = {}
mask = ""

for line in ins:
    line = line.split(" = ")
    if line[0] == "mask":
        mask = line[1]
    else:
        mem_index = int(line[0][4:-1])
        val = int(line[1])
        dexes = []
        apply_floating_mask(mem_index, mask)
        for d in dexes:
            mem[d] = val

s = 0
for m in mem:
    s += mem[m]

print(s)
