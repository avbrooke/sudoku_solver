import pprint

def solver(b):
    find = find_empty(b)
    if not find:
        return True

    row, col = find

    num = 1
    while num < 10:
        if validator(b, (row, col), num):
            b[row][col] = num

            if solver(b):
                return True

            b[row][col] = 0

        num += 1

    return False


def validator(b, pos, n):

    for i in range(0, len(b)):
        if b[pos[0]][i] == n and pos[1] != i:
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

def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)
    return None

def print_board(b):
    for i in range (len(b)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range (len(b[0])):
            if j % 3 == 0:
                print(" | ", end = "")

            if j == 8:
                print(b[i][j], end = "\n")
            else:
                print(str(b[i][j]) + " ", end = "")


board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

pp = pprint.PrettyPrinter(width = 41, compact = True)
solver(board)
pp.pprint(board)


