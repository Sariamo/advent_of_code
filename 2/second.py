def calculator(a, b):
    symbol_points = ["a", "b", "c"]
    symbol_points_losing = ["c", "a", "b"]
    symbol_points_winning = ["b", "c", "a"]
    if b == "x":
        return symbol_points.index(symbol_points_losing[symbol_points.index(a)]) + 1
    elif b == "y":
        return 3 + symbol_points.index(a) + 1
    else:
        return 6 + symbol_points.index(symbol_points_winning[symbol_points.index(a)]) + 1


p = 0
with open("decisions", "r") as d:
    for de in d.readlines():
        a = de.split(" ")[0].lower()
        b = de.split(" ")[1].replace("\n", "").lower()
        p += calculator(a, b)
print(p)
