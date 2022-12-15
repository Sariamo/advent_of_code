def fall(input):
    y_offset = 464
    fall_ctr = 0
    y_pos = 500 - y_offset
    while True:
        print(fall_ctr, y_pos)

        if input[fall_ctr][y_pos] == '.':
            input[fall_ctr][y_pos] = '+'
            if fall_ctr > 0:
                input[fall_ctr - 1][y_pos] = '.'
            fall_ctr += 1
            continue

        if input[fall_ctr][y_pos] == '#' or input[fall_ctr][y_pos] == '+':

            if input[fall_ctr][y_pos - 1] == '.':
                y_pos -= 1
                input[fall_ctr][y_pos] = '+'
                input[fall_ctr - 1][y_pos] = "."
                fall_ctr += 1
                continue

            elif input[fall_ctr][y_pos + 1] == '.':
                y_pos += 1
                input[fall_ctr][y_pos] = '+'
                input[fall_ctr - 1][y_pos] = "."
                fall_ctr += 1
                continue

            else:
                input[fall_ctr - 1][y_pos] = '+'
                break

    return input


def get_first_one_to_fall_out(input):

    sand_count = 0
    for _ in range(15):
        input = fall(input)

        for inp in input:
            print(str(inp).replace("'", "").replace("[", "").replace("]", "").replace(",", ""))
        print()
        sand_count += 1
        print(sand_count)


def convert_to_matrix(rocks):
    x_offset = 463
    y_offset = 14

    rock_matrix = [["." for _ in range(158)] for _ in range(72)]

    for rock_complex in rocks:

        for rock_row in range(len(rock_complex) - 1):

            rock_coords = rock_complex[rock_row]
            rock_coords_next = rock_complex[rock_row + 1]

            if rock_coords_next[0] - rock_coords[0] < 0:

                for i in range(rock_coords[0] - rock_coords_next[0]):
                    rock_matrix[rock_coords_next[0] + i - x_offset][rock_coords[1] - y_offset] = "#"

            if rock_coords_next[0] - rock_coords[0] > 0:

                for i in range(rock_coords_next[0] - rock_coords[0]):
                    rock_matrix[rock_coords[0] + i - x_offset][rock_coords[1] - y_offset] = "#"

            if rock_coords_next[1] - rock_coords[1] < 0:

                for i in range(rock_coords[1] - rock_coords_next[1]):
                    rock_matrix[rock_coords_next[0] - x_offset][rock_coords_next[1] + i - y_offset] = "#"

            if rock_coords_next[1] - rock_coords[1] > 0:

                for i in range(rock_coords_next[1] - rock_coords[1]):
                    rock_matrix[rock_coords[0] - x_offset][rock_coords[1] + i - y_offset] = "#"

    new_rock_matrix = [["." for _ in range(len(rock_matrix))] for _ in range(len(rock_matrix[0]))]

    for i in range(len(rock_matrix)):
        for j in range(len(rock_matrix[i])):
            new_rock_matrix[j][i] = rock_matrix[i][j]

    return new_rock_matrix


rocks = []
with open("input", "r") as d:
    for inp in d.readlines():
        rock_i = inp.split(" -> ")
        rocks_properly_formatted = []
        for single_falling in rock_i:
            rocks_properly_formatted.append(single_falling.split(","))
        rocks_int = []
        rocks.append(rocks_properly_formatted)

for rock in rocks:
    for ro in rock:
        for i, rock_axis in enumerate(ro):
            ro[i] = int(rock_axis.replace("\n", ""))


rock_matrix = convert_to_matrix(rocks)
print(get_first_one_to_fall_out(rock_matrix))
