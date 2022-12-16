def fall(input):
    y_offset = 262
    fall_ctr = 0
    y_pos = 500 - y_offset
    while True:

        if input[fall_ctr][y_pos] == '.':
            input[fall_ctr][y_pos] = '+'
            if fall_ctr > 0:
                input[fall_ctr - 1][y_pos] = '.'
            fall_ctr += 1
            continue

        if input[fall_ctr][y_pos] == '#' or input[fall_ctr][y_pos] == '°':

            if input[fall_ctr][y_pos - 1] == '.':
                y_pos -= 1
                input[fall_ctr][y_pos] = '+'
                input[fall_ctr - 1][y_pos + 1] = "."
                fall_ctr += 1
                continue

            elif input[fall_ctr][y_pos + 1] == '.':
                y_pos += 1
                input[fall_ctr][y_pos] = '+'
                input[fall_ctr - 1][y_pos - 1] = "."
                fall_ctr += 1
                continue

            else:
                input[fall_ctr - 1][y_pos] = '°'
                break

    return input


def get_first_one_to_fall_out(input):
    sand_count = 0
    while "°" not in input[0]:

        input = fall(input)
        sand_count += 1
        print(sand_count)
        print(str([[rock for rock in rocks] for rocks in rock_matrix]).count("°"))
    print(sand_count)
    print(str([[rock for rock in rocks] for rocks in rock_matrix]).count("°"))


def convert_to_matrix(rocks):

    lowest_value_x = None
    highest_value_x = None
    lowest_value_y = None
    highest_value_y = None

    for rock_row in rocks:
        for rock in rock_row:
            if lowest_value_x is None or rock[0] < lowest_value_x:
                lowest_value_x = rock[0]
            if highest_value_x is None or rock[0] > highest_value_x:
                highest_value_x = rock[0]
            if lowest_value_y is None or rock[1] < lowest_value_y:
                lowest_value_y = rock[1]
            if highest_value_y is None or rock[1] > highest_value_y:
                highest_value_y = rock[1]

    lowest_value_x -= 200
    highest_value_x += 200
    x_range = highest_value_x - lowest_value_x + 1
    y_range = highest_value_y - lowest_value_y + 1

    rock_matrix = [["." for _ in range(x_range)] for _ in range(y_range)]

    for rock_complex in rocks:

        for rock_index in range(len(rock_complex) - 1):

            rock_start = rock_complex[rock_index]
            rock_end = rock_complex[rock_index + 1]

            if rock_start[0] > rock_end[0]:
                for i in range(rock_start[0] - rock_end[0] + 1):
                    rock_matrix[rock_end[1] - lowest_value_y][rock_end[0] + i - lowest_value_x] = '#'
            if rock_start[0] < rock_end[0]:
                for i in range(rock_end[0] - rock_start[0] + 1):
                    rock_matrix[rock_start[1] - lowest_value_y][rock_start[0] + i - lowest_value_x] = '#'
            if rock_start[1] > rock_end[1]:
                for i in range(rock_start[1] - rock_end[1] + 1):
                    rock_matrix[rock_end[1] + i - lowest_value_y][rock_end[0] - lowest_value_x] = '#'
            if rock_start[1] < rock_end[1]:
                for i in range(rock_end[1] - rock_start[1] + 1):
                    rock_matrix[rock_start[1] + i - lowest_value_y][rock_start[0] - lowest_value_x] = '#'

    for _ in range(lowest_value_y):
        rock_matrix.insert(0, ["." for _ in range(x_range)])
    rock_matrix.insert(len(rock_matrix), ["." for _ in range(x_range)])
    rock_matrix.insert(len(rock_matrix), ["#" for _ in range(x_range)])
    return rock_matrix


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
