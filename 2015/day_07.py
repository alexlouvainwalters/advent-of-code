"""This file produces solutions to day 7 of Advent of Code."""


import copy


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    wires = {}
    for i in range(len(input_data)):
        input_data[i] = input_data[i].split(" -> ")
        if input_data[i][1] not in wires:
            input_data[i][1] = input_data[i][1].rstrip()
            wires[input_data[i][1]] = None
        input_data[i][0] = input_data[i][0].split()
        if len(input_data[i][0]) == 1 and input_data[i][0][0].isdigit():
            input_data[i][1] = input_data[i][1].rstrip()
            wires[input_data[i][1]] = int(input_data[i][0][0])
            input_data[i] = None

    complete = False
    while not complete:
        complete = True

        for i in range(len(input_data)):
            if input_data[i] is not None:
                complete = False
                calc = input_data[i][0]
                if len(calc) == 1:
                    if isinstance(calc[0], str):
                        if calc[0].isdigit():
                            calc[0] = int(calc[0])
                    if calc[0] in wires:
                        if wires[calc[0]] is not None:
                            calc[0] = wires[calc[0]]
                if len(calc) == 2:
                    if isinstance(calc[1], str):
                        if calc[1].isdigit():
                            calc[1] = int(calc[1])
                    if calc[1] in wires:
                        if wires[calc[1]] is not None:
                            calc[1] = wires[calc[1]]
                if len(calc) == 3:
                    if isinstance(calc[0], str):
                        if calc[0].isdigit():
                            calc[0] = int(calc[0])
                    if calc[0] in wires:
                        if wires[calc[0]] is not None:
                            calc[0] = wires[calc[0]]
                    if isinstance(calc[2], str):
                        if calc[2].isdigit():
                            calc[2] = int(calc[2])
                    if calc[2] in wires:
                        if wires[calc[2]] is not None:
                            calc[2] = wires[calc[2]]
                input_data[i][0] = calc

        for i in range(len(input_data)):
            if input_data[i] is not None:
                calc = input_data[i][0]
                if len(calc) == 1:
                    if isinstance(calc[0], int):
                        wires[input_data[i][1]] = calc[0]
                        input_data[i] = None
                elif len(calc) == 2 and calc[0] == "NOT":
                    if isinstance(calc[1], int):
                        wires[input_data[i][1]] = ~calc[1]
                        input_data[i] = None
                elif len(calc) == 3:
                    if isinstance(calc[0], int) and isinstance(calc[2], int):
                        if calc[1] == "AND":
                            wires[input_data[i][1]] = calc[0] & calc[2]
                            input_data[i] = None
                        elif calc[1] == "OR":
                            wires[input_data[i][1]] = calc[0] | calc[2]
                            input_data[i] = None
                        elif calc[1] == "LSHIFT":
                            wires[input_data[i][1]] = calc[0] << calc[2]
                            input_data[i] = None
                        elif calc[1] == "RSHIFT":
                            wires[input_data[i][1]] = calc[0] >> calc[2]
                            input_data[i] = None

    answer = str(wires["a"])

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    wires = {}
    for i in range(len(input_data)):
        input_data[i] = input_data[i].split(" -> ")
        if input_data[i][1] not in wires:
            input_data[i][1] = input_data[i][1].rstrip()
            wires[input_data[i][1]] = None
        input_data[i][0] = input_data[i][0].split()
        if len(input_data[i][0]) == 1 and input_data[i][0][0].isdigit():
            input_data[i][1] = input_data[i][1].rstrip()
            wires[input_data[i][1]] = int(input_data[i][0][0])
            input_data[i] = None

    input_data_default = copy.deepcopy(input_data)
    wires_default = copy.deepcopy(wires)

    complete = False
    reset = False
    while not reset or not complete:
        complete = True

        for i in range(len(input_data)):
            if input_data[i] is not None:
                complete = False
                calc = input_data[i][0]
                if len(calc) == 1:
                    if isinstance(calc[0], str):
                        if calc[0].isdigit():
                            calc[0] = int(calc[0])
                    if calc[0] in wires:
                        if wires[calc[0]] is not None:
                            calc[0] = wires[calc[0]]
                if len(calc) == 2:
                    if isinstance(calc[1], str):
                        if calc[1].isdigit():
                            calc[1] = int(calc[1])
                    if calc[1] in wires:
                        if wires[calc[1]] is not None:
                            calc[1] = wires[calc[1]]
                if len(calc) == 3:
                    if isinstance(calc[0], str):
                        if calc[0].isdigit():
                            calc[0] = int(calc[0])
                    if calc[0] in wires:
                        if wires[calc[0]] is not None:
                            calc[0] = wires[calc[0]]
                    if isinstance(calc[2], str):
                        if calc[2].isdigit():
                            calc[2] = int(calc[2])
                    if calc[2] in wires:
                        if wires[calc[2]] is not None:
                            calc[2] = wires[calc[2]]
                input_data[i][0] = calc

        for i in range(len(input_data)):
            if input_data[i] is not None:
                calc = input_data[i][0]
                if len(calc) == 1:
                    if isinstance(calc[0], int):
                        wires[input_data[i][1]] = calc[0]
                        input_data[i] = None
                elif len(calc) == 2 and calc[0] == "NOT":
                    if isinstance(calc[1], int):
                        wires[input_data[i][1]] = ~calc[1]
                        input_data[i] = None
                elif len(calc) == 3:
                    if isinstance(calc[0], int) and isinstance(calc[2], int):
                        if calc[1] == "AND":
                            wires[input_data[i][1]] = calc[0] & calc[2]
                            input_data[i] = None
                        elif calc[1] == "OR":
                            wires[input_data[i][1]] = calc[0] | calc[2]
                            input_data[i] = None
                        elif calc[1] == "LSHIFT":
                            wires[input_data[i][1]] = calc[0] << calc[2]
                            input_data[i] = None
                        elif calc[1] == "RSHIFT":
                            wires[input_data[i][1]] = calc[0] >> calc[2]
                            input_data[i] = None

        if not reset and complete:
            reset = True
            complete = False
            temp_a = wires["a"]
            input_data = copy.deepcopy(input_data_default)
            wires = copy.deepcopy(wires_default)
            wires["b"] = temp_a

    answer = str(wires["a"])

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_07.txt"))
    print("Part 2: " + part_2("day_07.txt"))


if __name__ == "__main__":
    main()
