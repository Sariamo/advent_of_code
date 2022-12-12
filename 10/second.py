def draw_crt(input):

    round = 0
    crt_line = ""
    sprite_pos = 0
    crt_pos = 0

    for cycle, height in input:
        if cycle % 40 == 0:
            print("\n")
            crt_line = ""

        # Start


        # During

        # End


input = []
with open("input", "r") as d:
    for inp in d.readlines():
        if inp.startswith("addx "):
            input.append(int(inp.replace("addx ", "")))
        else:
            input.append(0)

draw_crt(input)