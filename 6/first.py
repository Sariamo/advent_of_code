def all_different(a, b, c, d):
    return len({a, b, c, d}) == 4


with open("input", "r") as d:
    for inp in d.readlines():
        for i, x in enumerate(inp):
            if i >= 3 and all_different(x, inp[i-1], inp[i-2], inp[i-3]):
                print(i+1)
                break
