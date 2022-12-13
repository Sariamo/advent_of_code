def get_summed_cycle_strength(input):

    cycle_measure_numbers = [20, 60, 100, 140, 180, 220]
    x = 1
    res = 0
    round = 0

    for inp in input:
        round += 1

        if round in cycle_measure_numbers:
            res += x * round
            print("Cycle measure number! ", round, x, x * round, res)

        if inp != 0:
            round += 1

            if round in cycle_measure_numbers:
                res += x * round
                print("Cycle measure number! ", round, x, x * round, res)

            x += inp

    return res


input = []
with open("input", "r") as d:
    for inp in d.readlines():
        if inp.startswith("addx "):
            input.append(int(inp.replace("addx ", "")))
        else:
            input.append(0)


print(get_summed_cycle_strength(input))
