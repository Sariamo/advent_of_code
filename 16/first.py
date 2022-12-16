class Valve:
    def __init__(self, name, flow_rate, next_valves):
        self.name = name
        self.flow_rate = flow_rate
        self.next_valves = next_valves


def calculate(input):
    pressure_sum = 0
    open_valves = []
    current_valve = None
    valve_to_open = None
    for minute in range(1, 31):
        print()
        print("== Minute " + str(minute) + " ==")

        if len(open_valves) == len(input):
            update_pressure_sum(open_valves, pressure_sum)
            continue
        if not open_valves and not current_valve and not valve_to_open:
            print("No valves are open.")
            current_valve = input[0]
            if current_valve.flow_rate == 0:
                current_valve = get_highest_follow_valve(current_valve, input, open_valves)
                print("You move to valve " + current_valve.name + ".")
                continue

        if current_valve and not valve_to_open:
            if not open_valves:
                print("No valves are open.")
            else:
                update_pressure_sum(open_valves, pressure_sum)
            if current_valve not in open_valves:
                print("You open valve " + current_valve.name + ".")
            valve_to_open = current_valve
            current_valve = None

            continue
        if valve_to_open:
            if valve_to_open not in open_valves:
                open_valves.append(valve_to_open)
            pressure_sum = update_pressure_sum(open_valves, pressure_sum)

            current_valve = get_highest_follow_valve(valve_to_open, input, open_valves)
            print("You move to " + current_valve.name + ".")

            valve_to_open = None
    return pressure_sum


def update_pressure_sum(open_valves, pressure_sum):
    pressure = sum([valve.flow_rate for valve in open_valves])
    if len(open_valves) == 1:
        print("Valve " + open_valves[0].name + " is open, releasing " + str(open_valves[0].flow_rate) + " pressure.")
    else:
        print("Valves " + ", ".join([valve.name for valve in open_valves]) + " are open, releasing " + str(
            pressure) + " pressure.")
    pressure_sum += pressure
    return pressure_sum


def get_highest_follow_valve(current_valve, input, open_valves):
    valve_objs = []

    for v in current_valve.next_valves:
        valve_objs.append([valve for valve in input if valve.name == v][0])
    unused_valves = [valve for valve in valve_objs if valve not in open_valves]
    if unused_valves:
        valve_objs = unused_valves
    valve_flows = [valve.flow_rate for valve in valve_objs]
    follow_valve = valve_objs[valve_flows.index(max(valve_flows))]
    return follow_valve


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
    print([valve.next_valves for valve in input])

print(calculate(input))
