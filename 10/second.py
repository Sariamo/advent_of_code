def draw_crt(input):

    cycle = 0
    crt_matrix = []
    crt_line = ""
    sprite_pos = 1
    crt_pos = 0

    for height in input:
        if cycle % 40 == 0:
            crt_matrix.append(crt_line)
            crt_line = ""
            crt_pos = 0

        # Start
        cycle += 1
        print("Start cycle", str(cycle) + ": begin executing addx", height)

        if crt_pos in [sprite_pos - 1, sprite_pos, sprite_pos + 1]:
            crt_line += "#"
        else:
            crt_line += "."

        # During
        print("During cycle", str(cycle) + ": CRT draws pixel in position", crt_pos)
        crt_pos += 1

        # End
        print("Current CRT row:", crt_line)
        print()

        if height != 0:

            if cycle % 40 == 0:
                crt_matrix.append(crt_line)
                crt_line = ""
                crt_pos = 0

            # Begin
            cycle += 1

            # During
            if crt_pos in [sprite_pos - 1, sprite_pos, sprite_pos + 1]:
                crt_line += "#"
            else:
                crt_line += "."

            print("During cycle", str(cycle) + " CRT draws pixel in position", crt_pos)
            crt_pos += 1

            print("Current CRT row:", crt_line)

            # End
            sprite_pos += height
            print("End of cycle", str(cycle) + ": finish executing addx", str(height) + " (Register X is now " + str(sprite_pos) + ")")
            print()
    crt_matrix.append(crt_line)
    for crt_line in crt_matrix:
        print(crt_line)


input = []
with open("input", "r") as d:
    for inp in d.readlines():
        if inp.startswith("addx "):
            input.append(int(inp.replace("addx ", "")))
        else:
            input.append(0)

draw_crt(input)