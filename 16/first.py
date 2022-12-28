import random


class Valve:
    def __init__(self, name, flow_rate, next_valves):
        self.name = name
        self.flow_rate = flow_rate
        self.next_valves = next_valves


def calculate(input):
    pressure_sum = 0
    open_valves = []
    current_valve = input[0]
    valve_to_open = None
    sums = []
    for minute in range(1, 31):

        # print()
        # print("== Minute " + str(minute) + " ==")

        if len(open_valves) == len([v for v in input]):
            sum = update_pressure_sum(open_valves, pressure_sum)
            sums.append(sum)
            pressure_sum = sum

        elif current_valve and not valve_to_open:
            if not open_valves:
                sums.append(0)
                # print("No valves are open.")
            else:
                sum = update_pressure_sum(open_valves, pressure_sum)
                sums.append(sum)
                pressure_sum = sum
            if current_valve and random.random() > 0.5:
                # print("You open valve " + current_valve.name + ".")
                valve_to_open = current_valve
            else:
                current_valve = get_highest_follow_valve(current_valve, input, open_valves)
                # print("You move to " + current_valve.name + ".")

        elif valve_to_open:

            if valve_to_open not in open_valves:
                open_valves.append(valve_to_open)
            sum = update_pressure_sum(open_valves, pressure_sum)
            sums.append(sum)
            pressure_sum = sum

            current_valve = get_highest_follow_valve(valve_to_open, input, open_valves)
            # print("You move to " + current_valve.name + ".")

            valve_to_open = None

    return pressure_sum, sums


def update_pressure_sum(open_valves, pressure_sum):
    pressure = sum([valve.flow_rate for valve in open_valves])
    # if len(open_valves) == 1:
    #     print("Valve " + open_valves[0].name + " is open, releasing " + str(open_valves[0].flow_rate) + " pressure.")
    # else:
    #     print("Valves " + ", ".join(sorted([valve.name for valve in open_valves])) + " are open, releasing " + str(
    #         pressure) + " pressure.")
    pressure_sum += pressure
    return pressure_sum


def get_obj_from_str(input, valve_str):
    names = [valve.name for valve in input]
    return input[names.index(valve_str)]


def get_highest_follow_valve(current_valve, input, open_valves):
    return get_obj_from_str(input,  random.choice(current_valve.next_valves))
    # valve_objs = []
    #
    # for v in current_valve.next_valves:
    #     valve_objs.append([valve for valve in input if valve.name == v][0])
    # unused_valves = [valve for valve in valve_objs if valve not in open_valves]
    # if unused_valves:
    #     valve_objs = unused_valves
    #
    # max_flow_rates = []
    # for valve in valve_objs:
    #     flow_rate = valve.flow_rate
    #     max_flow_rate = 0
    #     for next_valve in valve.next_valves:
    #         next_valve_obj = get_obj_from_str(input, next_valve)
    #         flow_rate_combined = 0
    #         if next_valve_obj not in open_valves:
    #             flow_rate_combined = flow_rate + next_valve_obj.flow_rate
    #         if max_flow_rate < flow_rate_combined:
    #             max_flow_rate = flow_rate_combined
    #     max_flow_rates.append(max_flow_rate)
    #
    # follow_valve = valve_objs[max_flow_rates.index(max(max_flow_rates))]
    # return follow_valve


input = []
with open("input", "r") as d:
    for inp in d.readlines():
        name = inp.split("Valve ")[1].split(" has")[0]
        flow_rate = int(inp.split("=")[1].split(";")[0])
        next_valves = inp.split("valve")[1].replace("\n", "").strip()
        if ", " in next_valves:
            next_valves = next_valves.replace("s ", "").split(", ")
            for v_i, valve in enumerate(next_valves):
                next_valves[v_i] = valve.strip().replace("\n", "")
        else:
            next_valves = [next_valves]

        input.append(Valve(name, flow_rate, next_valves))
max = 0
while True:
    value, sums = calculate(input)
    if value > max:
        max = value
        print(max, sums)
