f = open("test.txt", "r")
seats = [list(s.strip()) for s in f.readlines()]
f.close()

def occupied(seats, row, col):
    if not ((0 <= row < len(seats)) and (0 <= col < len(seats[0]))):
        return 0
    elif seats[row][col] == '#':
        return 1
    return 0

def occupied_line(seats, row, col, xdir, ydir):
    for i in range(1, max(len(seats), len(seats[0]))+1):
        r = row + (xdir * i)
        c = col + (ydir * i)
        if not ((0 <= r < len(seats)) and (0 <= c < len(seats[0]))):
            return 0
        elif seats[r][c] == '#':
            return 1
        elif seats[r][c] == 'L':
            return 0
    return 0


def count_occupied_adjacent(seats, row, col):
    occ = 0
    occ += occupied(seats, row-1, col-1)
    occ += occupied(seats, row-1, col)
    occ += occupied(seats, row-1, col+1)
    occ += occupied(seats, row, col-1)
    occ += occupied(seats, row, col+1)
    occ += occupied(seats, row+1, col-1)
    occ += occupied(seats, row+1, col)
    occ += occupied(seats, row+1, col+1)
    return occ

def count_occupied_visible(seats, row, col):
    occ = 0
    occ += occupied_line(seats, row, col, -1, -1)
    occ += occupied_line(seats, row, col, -1, 0)
    occ += occupied_line(seats, row, col, -1, 1)
    occ += occupied_line(seats, row, col, 0, -1)
    occ += occupied_line(seats, row, col, 0, 1)
    occ += occupied_line(seats, row, col, 1, -1)
    occ += occupied_line(seats, row, col, 1, 0)
    occ += occupied_line(seats, row, col, 1, 1)
    return occ

def adjust(seats):
    new_seats = []
    for row in range(len(seats)):
        new_seats.append([])
        for col in range(len(seats[row])):
            if seats[row][col] == '.':
                new_seats[-1].append('.')
            elif count_occupied_adjacent(seats, row, col) == 0 and seats[row][col] == 'L':
                new_seats[-1].append('#')
            elif count_occupied_adjacent(seats, row, col) >= 4 and seats[row][col] == '#':
                new_seats[-1].append('L')
            else:
                new_seats[-1].append(seats[row][col])
    return new_seats

def adjust_new(seats):
    new_seats = []
    for row in range(len(seats)):
        new_seats.append([])
        for col in range(len(seats[row])):
            if seats[row][col] == '.':
                new_seats[-1].append('.')
            elif count_occupied_visible(seats, row, col) == 0 and seats[row][col] == 'L':
                new_seats[-1].append('#')
            elif count_occupied_visible(seats, row, col) >= 5 and seats[row][col] == '#':
                new_seats[-1].append('L')
            else:
                new_seats[-1].append(seats[row][col])
    return new_seats

def count_occupied_total(seats):
    return sum([sum([1 for c in row if c == "#"]) for row in seats])

def check_match(seats, new_seats):
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] != new_seats[row][col]:
                return False
    return True

# new_seats = adjust(seats)

new_seats = adjust_new(seats)

while not check_match(seats, new_seats):
    seats = new_seats
    # new_seats = adjust(seats)
    new_seats = adjust_new(seats)

print(count_occupied_total(new_seats))



# print("\n".join(["".join(row) for row in new_seats]))
