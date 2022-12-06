def all_different(l):
    return len(l) == len(set(l))


with open("input", "r") as d:
    for inp in d.readlines():
        for i, x in enumerate(inp):
            if i >= 13 and all_different(list(inp[i-13:i+1])):

                print(i+1)
                break
