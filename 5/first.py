def add_stacks(input):
    stacks = ["" for _ in range(9)]
    i = 0
    index = 0
    while i < len(input):
        if input[i] == "[":
            stacks[index] = input[i + 1]
            i += 1
            continue
        if input[i] == " ":
            num_of_spaces = 0
            while input[i] == " ":
                num_of_spaces += 1
                i += 1
            num_of_spaces += 5
            for _ in range(num_of_spaces // 4):
                index += 1
        else:
            i += 1
    return stacks


def filter_input(input):
    input = input.replace("move ", "").replace(" from", "").replace(" to", "").replace("\n", "")
    input_list = input.split(" ")
    input_list_ints = []
    for i in input_list:
        input_list_ints.append(int(i))
    return input_list_ints


def execute_instructions(stacks, instructions):
    for ins in instructions:
        print(stacks)
        for _ in range(ins[0]):
            moving_obj = stacks[ins[1] - 1][-1]
            stacks[ins[1] - 1].pop()
            stacks[ins[2] - 1].append(moving_obj)
    res = ""
    for s in stacks:
        res += s[-1]
    return res


read_part_one = True
instructions = []
stacks = []
with open("input", "r") as input:
    for i in input.readlines():
        if i == "\n":
            continue
        if "1   2   3   4   5   6   7   8   9" in i:
            read_part_one = False
            continue
        if read_part_one:
            stacks.append(add_stacks(i))
        else:
            instructions.append(filter_input(i))

stacks_new = [["" for _ in range(8)] for _ in range(9)]
for i, stack in enumerate(stacks):
    for j, stack_el in enumerate(stack):
        stacks_new[j][i] = stack_el

stacks_without_spaces = []
for stack in stacks_new:
    stack_without_spaces = []
    for stack_el in stack:
        if stack_el != "":
            stack_without_spaces.append(stack_el)
    stacks_without_spaces.append(stack_without_spaces)

for i, stack in enumerate(stacks_new):
    stack.reverse()

final_tops = execute_instructions(stacks_without_spaces, instructions)

print(final_tops)
