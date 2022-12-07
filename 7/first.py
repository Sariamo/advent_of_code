def get_sum_of_subdir(tree, i):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dir_size = 0
    i += 1
    l = tree[i]
    while l[0] != "$" and not i == len(tree) - 1:
        l = tree[i]
        print(l)
        if l[0] in numbers:
            dir_size += int(l.split(" ")[0])
        if l.startswith("dir "):
            demanded_dir = l.split("dir ")[1]
            dir_i = tree.index("$ cd " + demanded_dir) + 1
            dir_size += get_sum_of_subdir(tree, dir_i)
        if i < len(tree) - 1:
            i += 1
    if dir_size <= 100000:
        return dir_size
    return 0


def get_file_sum_under_100000(tree):
    total_size = 0

    for i, l in enumerate(tree):
        if l == "$ ls\n":
            total_size += get_sum_of_subdir(tree, i)

    return total_size


with open("input", "r") as d:
    tree = []
    files_size_sum_folders_under_100000 = 0
    for inp in d.readlines():
        tree.append(inp)
    files_size_sum_folders_under_100000 = get_file_sum_under_100000(tree)

print(files_size_sum_folders_under_100000)
