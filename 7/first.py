import random


def get_tree_structure(input):
    tree = []
    input_index = 0
    subdir = []
    while input_index < len(input):
        if "cd .." in inp:
            tree.append(subdir)
            subdir = []
        elif "cd" in inp:

            pass
        elif "dir" in inp:
            pass
        else:


        return tree


def get_file_sum_under_100000(tree):
    sum = 0

    return sum


with open("input", "r") as d:
    input = []
    for inp in d.readlines():
        input.append(inp)

tree = get_tree_structure(input)
print(files_size_sum_folders_under_100000)
