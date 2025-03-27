import pprint

def solver(b):
    find = find_empty(b)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if validator(b, (row, col), i):
            b[row][col] = i

            if solver(b):
                return True

            b[row][col] = 0

        return False


def validator(b, pos, n):

    for i in range(0, len(b)):
        if b[pos[0]][i] == n and p[1] != i:
            return False

    for i in range(0, len(b)):
        if b[i][pos[1]] == n and pos[1] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range (box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x *3 +3):
            if b[i][j] == n and (i,j) != pos:
                return False
    return True

