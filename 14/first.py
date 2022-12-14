def fall(input):
    pass


def get_first_one_to_fall_out(input):
    map = []


falling = []
with open("input", "r") as d:
    for inp in d.readlines():
        falling_i = inp.split(" -> ")
        falling_properly_formatted = []
        for single_falling in falling_i:
            falling_properly_formatted.append(single_falling.split(","))
        falling_int = []
        falling.append(falling_properly_formatted)

for fall_path in falling:
    for fall in fall_path:
        for i, fall_axis in enumerate(fall):
            fall[i] = int(fall_axis.replace("\n", ""))

print(get_first_one_to_fall_out(input()))