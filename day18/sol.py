f = open("train.txt", "r")
probs = [[a for a in list(p) if (a != " " and a != "\n")] for p in f.readlines()]
f.close()

def solve(prob):
    val = 0
    op = ""
    while len(prob) > 0:
        p = prob.pop(0)
        if p == "(":
            if op == "*":
                val *= solve(prob)
            else:
                val += solve(prob)
        elif p == ")":
            return val
        elif p.isnumeric():
            if op == "*":
                val *= int(p)
            else:
                val += int(p)
        else:
            op = p
    return val

#s = 0

#for p in probs:
#    s += solve(p)

#print(s)

def precedence_preprocess(p):
    i = 0
    while i < len(p):
        if p[i] == "+":
            if p[i-1] != ")" and p[i+1] != "(":
                p.insert(i-1, "(")
                p.insert(i+3, ")")
                i += 1
            elif p[i-1] == ")" and p[i+1] != "(":
                if p[i+2] != ")":
                    close = 0
                    for j in range(i):
                        if p[i-j] == "(" and close == 0:
                            p.insert(i-j, "(")
                            close = -1
                        elif p[i-j] == "(":
                            close -= 1
                        elif p[i-j] == ")":
                            close += 1
                    if close != -1:
                        p.insert(0, "(")
                    p.insert(i+3, ")")
                    i += 1
            elif p[i-1] != ")" and p[i+1] == "(":
                p.insert(i-1, "(")
                j = p.index(")", i)
                p.insert(j, ")")
                i += 1
        i += 1
    print(" ".join(p))
    return p

s = 0

for p in probs:
    p = precedence_preprocess(p)
    print(solve(p))
    #s += solve(p)

print(s)

#5 + (8 * ((3 + 9) + 3) * 4 * 3)

#5 + (8 * 3 + 9 + 3 * 4 * 3)

#(5 + (8 * 3 + 9 + 3 * 4 * 3))

#(5 + (8 * (3 + 9) + 3 * 4 * 3))

#(5 + (8 * ((3 + 9) + 3) * 4 * 3))

#(((5 + (8 * (((3 + 9) + ) ) 3 * 4 * 3 ) )

#((((((2 + 4) * 9) * ((6 + 9) * (8 + 6))) + 6) + 2) + 4) * 2
