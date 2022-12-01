with open("calories", "r") as c:

    sum = 0
    values = []

    for i, cal in enumerate(c.readlines()):
        if cal != "\n":
            sum += int(cal)
        else:
            values.append(sum)
            sum = 0

values = sorted(values, reverse=True)
top_three = values[0] + values[1] + values[2]
print(top_three)