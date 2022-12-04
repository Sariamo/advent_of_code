def counter(inp):
    pair_one = inp.split(",")[0]
    pair_two = inp.split(",")[1]

    pair_one_lower = int(pair_one.split("-")[0])
    pair_one_upper = int(pair_one.split("-")[1])

    pair_two_lower = int(pair_two.split("-")[0])
    pair_two_upper = int(pair_two.split("-")[1])

    if pair_one_lower >= pair_two_lower and pair_two_upper >= pair_one_upper or \
        pair_two_lower >= pair_one_lower and pair_one_upper >= pair_two_upper:
        return 1
    else:
        return 0


p = 0
with open("ranges", "r") as d:
    for inp in d.readlines():
        p += counter(inp)
print(p)
