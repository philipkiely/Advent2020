f = open("test.txt", "r")
s = [list(l.strip()) for l in f.readlines()]
f.close()

dim = [s]

def active_bors(dim, z, x, y):
    active = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if not all([v == 0 for v in [i, j, k]]):
                    try:
                        if dim[z+i][x+j][y+k] == "#":
                            active += 1
                    except:  # Index out of range, so not active
                        pass
    return active
    

def sim(dim):
    new_z = []
    for z in range(len(dim)):
        new_x = []
        for x in range(len(dim[z])):
            new_y = []
            for y in range(len(dim[z][x])):
                cur = dim[z][x][y]
                a = active_bors(dim, z, x, y)
                if cur == "#" and a != 2 and a != 3:
                    new_y.append(".")
                elif cur == "." and a == 3:
                    new_y.append("#")
                else:
                    new_y.append(cur)
            new_x.append(new_y)
        new_z.append(new_x)
    return new_z


def expand(dim):
    new_z = []
    for z in range(len(dim)):
        new_x = []
        for x in range(len(dim[z])):
            y_buffer = ["."]
            new_y = y_buffer + dim[z][x] + y_buffer
            new_x.append(new_y)
        x_buffer = [["." for x in range(len(dim[z][0])+2)]]
        new_x = x_buffer + new_x + x_buffer
        new_z.append(new_x)
    z_buffer = [[["." for x in range(len(dim[z][0])+2)] for y in range(len(dim[0])+2)]]
    new_z = z_buffer + new_z + z_buffer
    return new_z

def count_active(dim):
    active = 0
    for z in dim:
        for x in z:
            for y in x:
                if y == "#":
                    active += 1
    return active

for i in range(6):
    """for d in dim:
        for r in d:
            print("".join(r))
        print("\n")
    print("\n\n")"""
    dim = expand(dim)
    dim = sim(dim)

print(count_active(dim))

dim = [[s]]


def active_bors_4d(dim, w, z, x, y):
    active = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if not all([v == 0 for v in [i, j, k, l]]):
                        try:
                            if dim[w+i][z+j][x+k][y+l] == "#":
                                active += 1
                        except:  # Index out of range, so not active
                            pass
    return active


def sim_4d(dim):
    new_w = []
    for w in range(len(dim)):
        new_z = []
        for z in range(len(dim[w])):
            new_x = []
            for x in range(len(dim[w][z])):
                new_y = []
                for y in range(len(dim[w][z][x])):
                    cur = dim[w][z][x][y]
                    a = active_bors_4d(dim, w, z, x, y)
                    if cur == "#" and a != 2 and a != 3:
                        new_y.append(".")
                    elif cur == "." and a == 3:
                        new_y.append("#")
                    else:
                        new_y.append(cur)
                new_x.append(new_y)
            new_z.append(new_x)
        new_w.append(new_z)
    return new_w


def expand_4d(dim):
    new_w = []
    for w in range(len(dim)):
        new_z = []
        for z in range(len(dim[w])):
            new_x = []
            for x in range(len(dim[w][z])):
                y_buffer = ["."]
                new_y = y_buffer + dim[w][z][x] + y_buffer
                new_x.append(new_y)
            x_buffer = [["." for x in range(len(dim[w][z][0])+2)]]
            new_x = x_buffer + new_x + x_buffer
            new_z.append(new_x)
        z_buffer = [[["." for x in range(len(dim[w][z][0])+2)]
                    for y in range(len(dim[w][0])+2)]]
        new_z = z_buffer + new_z + z_buffer
        new_w.append(new_z)
    w_buffer = [[[["." for x in range(len(dim[w][z][0])+2)] for y in range(len(dim[w][0])+2)] for x in range(len(dim[0])+2)]]
    new_w = w_buffer + new_w + w_buffer
    return new_w

def count_active_4d(dim):
    active = 0
    for w in dim:
        for z in w:
            for x in z:
                for y in x:
                    if y == "#":
                        active += 1
    return active


for i in range(6):
    """for d in dim:
        for r in d:
            print("".join(r))
        print("\n")
    print("\n\n")"""
    dim = expand_4d(dim)
    dim = sim_4d(dim)

print(count_active_4d(dim))
