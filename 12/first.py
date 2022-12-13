import random


def get_fewest_steps(matrix):
    alphabet = ['S', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    row, column = 0, 0

    for r, height_x in enumerate(matrix):
        for c, height_y in enumerate(matrix[row]):
            if matrix[r][c] == "S":
                row, column = r, c
                break

    used_fields = [[row, column]]
    steps = 0

    while matrix[row][column] != "E":

        steps += 1

        possible_directions = []
        if row > 0 and matrix[row - 1][column] == "E" or row < len(matrix) - 1 and matrix[row + 1][column] == "E" \
                or column > 0 and matrix[row][column - 1] == "E" or column < len(matrix[row]) - 1 and matrix[row][column + 1] == "E":
            return steps

        if row > 0 and [row - 1, column] not in used_fields and \
                alphabet.index(matrix[row - 1][column]) == alphabet.index(matrix[row][column]) or \
                len(alphabet) > alphabet.index(matrix[row][column]) + 1 == alphabet.index(matrix[row - 1][column]):
            possible_directions.append("up")
        if row < len(matrix) and [row + 1, column] not in used_fields and \
                alphabet.index(matrix[row + 1][column]) == alphabet.index(matrix[row][column]) or \
                len(alphabet) > alphabet.index(matrix[row][column]) + 1 == alphabet.index(matrix[row + 1][column]):
            possible_directions.append("down")
        if column > 0 and [row, column - 1] not in used_fields and \
                alphabet.index(matrix[row][column - 1]) == alphabet.index(matrix[row][column]) or \
                len(alphabet) > alphabet.index(matrix[row][column - 1]) + 1 == alphabet.index(matrix[row][column]):
            possible_directions.append("left")
        if column < len(matrix[row]) and [row, column + 1] not in used_fields and \
                alphabet.index(matrix[row][column + 1]) == alphabet.index(matrix[row][column]) or \
                len(alphabet) > alphabet.index(matrix[row][column + 1]) + 1 == alphabet.index(matrix[row][column]):
            possible_directions.append("right")
        print(possible_directions)
        if not possible_directions:
            break

        chosen_dir = random.choice(possible_directions)
        if chosen_dir == "up":
            row, column = row - 1, column
        if chosen_dir == "down":
            row, column = row + 1, column
        if chosen_dir == "left":
            row, column = row, column - 1
        if chosen_dir == "right":
            row, column = row, column + 1
        used_fields.append([row, column])


input = []
with open("input", "r") as d:
    for inp in d.readlines():
        input.append(inp.replace("\n", ""))

lowest_ever = None
for _ in range(1):
    steps = get_fewest_steps(input)
    if steps is None:
        continue
    if lowest_ever is None:
        lowest_ever = steps
        print(lowest_ever)
    elif lowest_ever > steps:
        lowest_ever = steps
        print(lowest_ever)
