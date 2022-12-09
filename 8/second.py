def is_visible(forest, i, j):

    last_left = i
    last_right = len(forest) - 1 - i
    last_top = j
    last_bottom = len(forest[i]) - 1 - j

    for left in range(0, i):
        if forest[left][j] >= forest[i][j]:
            last_left = i - left

    for right in range(i + 1, len(forest)):
        if forest[right][j] >= forest[i][j]:
            last_right = i - right
            break

    for top in range(0, j):
        if forest[i][top] >= forest[i][j]:
            last_top = top - j

    for bottom in range(j + 1, len(forest[i])):
        if forest[i][bottom] >= forest[i][j]:
            last_bottom = bottom - j
            break

    return last_left * last_right * last_top * last_bottom


forest = []
with open("input", "r") as d:
    for inp in d.readlines():
        tress_row = []
        for tree in inp:
            if tree != "\n":
                tress_row.append(tree)
        forest.append(tress_row)

high_score = 0
for i, trees_row in enumerate(forest):
    visible_row = []
    for j, tree in enumerate(trees_row):
        score = is_visible(forest, i, j)
        if score > high_score:
            high_score = score

print(high_score)
