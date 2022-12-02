with open("calories", "r") as c:
    sum = 0
    highest_index = -1
    highest_val = 0
    for i, cal in enumerate(c.readlines()):
        if cal != "\n":
            sum += int(cal)
        elif sum > highest_val:
            highest_index = i
            highest_val = sum
            sum = 0
        elif cal == "\n":
            sum = 0

print(highest_val)