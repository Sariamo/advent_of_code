def calculator(inp):
    ctr = 0
    val = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    first = inp[:len(inp) // 2]
    second = inp[len(inp) // 2:]

    for v in val:
        if v in first and v in second:
           ctr += val.index(v) + 1
    return ctr


p = 0
with open("input", "r") as d:
    for inp in d.readlines():
        p += calculator(inp)
print(p)
