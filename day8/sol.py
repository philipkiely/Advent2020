f = open("test.txt", "r")
instructions = f.readlines()
f.close()

def run(ins):
    score = 0
    count = 1
    ex = {}
    i = 0
    while True:
        if i in ex:
            #print(score)
            #print(i)
            #print(count)
            return
        ex[i] = count
        if ins[i][:3] == "acc":
            score += int(ins[i][4:])
        elif ins[i][:3] == "jmp":
            i += int(ins[i][4:]) - 1
        i += 1
        count += 1
        if i == len(ins):
            print("score", score)
            return

# run(instructions)

for j in range(len(instructions)):
    if instructions[j][:3] == "nop":
        instructions[j] = "jmp" + instructions[j][3:]
    elif instructions[j][:3] == "jmp":
        instructions[j] = "nop"  + instructions[j][3:]
    run(instructions)
    if instructions[j][:3] == "nop":
        instructions[j] = "jmp" + instructions[j][3:]
    elif instructions[j][:3] == "jmp":
        instructions[j] = "nop" + instructions[j][3:]
