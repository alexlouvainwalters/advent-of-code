"""This file produces solutions to day 12 of Advent of Code."""


import json


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    data = json.loads(input_data)

    total = 0
    stack = [data]

    while stack:
        x = stack.pop()

        if isinstance(x, int):
            total += x
        elif isinstance(x, list):
            stack.extend(x)
        elif isinstance(x, dict):
            stack.extend(x.values())

    answer = str(total)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    data = json.loads(input_data)

    total = 0
    stack = [data]

    while stack:
        x = stack.pop()

        if isinstance(x, int):
            total += x
        elif isinstance(x, list):
            stack.extend(x)
        elif isinstance(x, dict):
            if "red" not in x.values():
                stack.extend(x.values())

    answer = str(total)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_12.txt"))
    print("Part 2: " + part_2("day_12.txt"))


if __name__ == "__main__":
    main()
