f = open("test.txt", "r")
ins = [d.strip("\n") for d in f.readlines()]
f.close()

dirs = {"N": 0, "E": 90, "S": 180, "W": 270}

facing = 90

pos = [0, 0] #N, E

for i in ins:
    if i[0] == "R":
        facing += int(i[1:])
        facing = facing % 360
    elif i[0] == "L":
        facing -= int(i[1:])
        facing = facing % 360
    elif i[0] == "F":
        if facing % 180 == 0:
            pos[0] += ((90 - facing) / 90) * int(i[1:])
        else:
            pos[1] += ((180 - facing) / 90) * int(i[1:])
    elif i[0] == "N":
        pos[0] += int(i[1:])
    elif i[0] == "E":
        pos[1] += int(i[1:])
    elif i[0] == "S":
        pos[0] -= int(i[1:])
    elif i[0] == "W":
        pos[1] -= int(i[1:])

print(pos)

print(int(abs(pos[0])) + int(abs(pos[1])))

pos = [0, 0]

waypoint = [1, 10]

for i in ins:
    if i[0] == "R":
        amt = (int(i[1:]) % 360) / 90
        for a in range(int(amt)):
            tmp = waypoint[0]
            waypoint[0] = -1 * waypoint[1]
            waypoint[1] = tmp
    elif i[0] == "L":
        amt = (int(i[1:]) % 360) / 90
        for a in range(int(amt)):
            tmp = waypoint[1]
            waypoint[1] = -1 * waypoint[0]
            waypoint[0] = tmp
    elif i[0] == "F":
        pos[0] += waypoint[0] * int(i[1:])
        pos[1] += waypoint[1] * int(i[1:])
    elif i[0] == "N":
        waypoint[0] += int(i[1:])
    elif i[0] == "E":
        waypoint[1] += int(i[1:])
    elif i[0] == "S":
        waypoint[0] -= int(i[1:])
    elif i[0] == "W":
        waypoint[1] -= int(i[1:])

print(pos)

print(int(abs(pos[0])) + int(abs(pos[1])))
