def calculator(inp):
    ctr = 0
    val = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for v in val:
        if v in inp[0] and v in inp[1] and v in inp[2]:
           ctr += val.index(v) + 1
    return ctr


p = 0
with open("input", "r") as d:
    input = ['', '', '']
    index = 0
    for inp in d.readlines():
        input[index] = inp
        if index == 2:
            p += calculator(input)
            index = 0
        else:
            index += 1
print(p)
