def calculator(a, b):
    symbol_points = ["x", "y", "z"]
    if a == "a" and b == "y" or a == "b" and b == "z" or a == "c" and b == "x":
        return 6 + symbol_points.index(b) + 1
    elif a == "a" and b == "x" or a == "b" and b == "y" or a == "c" and b == "z":
        return 3 + symbol_points.index(b) + 1
    else:
        return symbol_points.index(b) + 1


p = 0
with open("decisions", "r") as d:
    for de in d.readlines():
        a = de.split(" ")[0].lower()
        b = de.split(" ")[1].replace("\n", "").lower()
        p += calculator(a, b)
print(p)
