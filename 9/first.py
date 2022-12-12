


p = 0
with open("ranges", "r") as d:
    for inp in d.readlines():
        p += counter(inp)
print(p)
