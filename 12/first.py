def get_cost(matrix, p):
    dest = []
    for i, row in enumerate(matrix):
        if "S" in matrix[i]:
            dest = [i, row.index("S")]
            break
    return abs(dest[0] - p[0]) + abs(dest[1] - p[1])


def get_field_with_minimum_cost(matrix, queue):
    min_cost = None
    min_cost_field = None
    for q in queue:
        cost = get_cost(matrix, q)
        if min_cost is None or cost < min_cost:
            min_cost = cost
            min_cost_field = q
    return min_cost_field


def is_reachable(matrix, a, b):
    alphabet = ['S', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'E']

    return 0 <= b[0] <= len(matrix) and 0 <= b[1] <= len(matrix[0]) \
        and alphabet.index(matrix[a[0][a[1]]]) + 1 >= alphabet.index(matrix[b[0][b[1]]])


def get_reachable_neighbors(matrix, a):
    reachable_neighbors = []
    if is_reachable(matrix, a, [a[0] + 1, a[1]]):
        reachable_neighbors.append([a[0] + 1, a[1]])
    if is_reachable(matrix, a, [a[0] - 1, a[1]]):
        reachable_neighbors.append([a[0] - 1, a[1]])
    if is_reachable(matrix, a, [a[0], a[1] - 1]):
        reachable_neighbors.append([a[0], a[1] - 1])
    if is_reachable(matrix, a, [a[0], a[1] + 1]):
        reachable_neighbors.append([a[0], a[1] + 1])

    return reachable_neighbors


def get_fewest_steps(matrix):
    row, column = 0, 0

    for r, height_x in enumerate(matrix):
        for c, height_y in enumerate(matrix[row]):
            if matrix[r][c] == "S":
                row, column = r, c
                break

    # Dijkstra
    start = [row, column]
    used_fields = []
    queue = [get_reachable_neighbors(matrix, start)]
    steps = 0

    while queue:

        steps += 1

        min_cost_neighbor = get_field_with_minimum_cost(matrix, queue)
        new_fields = get_reachable_neighbors(matrix, min_cost_neighbor)

    # Own heuristic

    # while matrix[row][column] != "E":
    #
    #     steps += 1
    #
    #     possible_directions = []
    #     if row > 0 and matrix[row - 1][column] == "E" or row < len(matrix) - 1 and matrix[row + 1][column] == "E" \
    #             or column > 0 and matrix[row][column - 1] == "E" or column < len(matrix[row]) - 1 and \
    #             matrix[row][column + 1] == "E":
    #         return steps

    #     if row > 0 and [row - 1, column] not in used_fields and \
    #             alphabet.index(matrix[row - 1][column]) == alphabet.index(matrix[row][column]) or \
    #             len(alphabet) > alphabet.index(matrix[row][column]) + 1 == alphabet.index(matrix[row - 1][column]):
    #         possible_directions.append("up")
    #     if row < len(matrix) and [row + 1, column] not in used_fields and \
    #             alphabet.index(matrix[row + 1][column]) == alphabet.index(matrix[row][column]) or \
    #             len(alphabet) > alphabet.index(matrix[row][column]) + 1 == alphabet.index(matrix[row + 1][column]):
    #         possible_directions.append("down")
    #     if column > 0 and [row, column - 1] not in used_fields and \
    #             alphabet.index(matrix[row][column - 1]) == alphabet.index(matrix[row][column]) or \
    #             len(alphabet) > alphabet.index(matrix[row][column - 1]) + 1 == alphabet.index(matrix[row][column]):
    #         possible_directions.append("left")
    #     if column < len(matrix[row]) and [row, column + 1] not in used_fields and \
    #             alphabet.index(matrix[row][column + 1]) == alphabet.index(matrix[row][column]) or \
    #             len(alphabet) > alphabet.index(matrix[row][column + 1]) + 1 == alphabet.index(matrix[row][column]):
    #         possible_directions.append("right")
    #     print(possible_directions)
    #     if not possible_directions:
    #         break
    #
    #     chosen_dir = random.choice(possible_directions)
    #     if chosen_dir == "up":
    #         row, column = row - 1, column
    #     if chosen_dir == "down":
    #         row, column = row + 1, column
    #     if chosen_dir == "left":
    #         row, column = row, column - 1
    #     if chosen_dir == "right":
    #         row, column = row, column + 1
    #     used_fields.append([row, column])


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
