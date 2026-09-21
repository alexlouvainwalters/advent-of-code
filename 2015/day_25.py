"""This file produces solutions to day 25 of Advent of Code."""


import re


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    location = re.findall(r"\d+", input_data)

    row = int(location[1])
    column = int(location[0])

    code_number = 0

    for i in range(row + 1):
        code_number += i

    for i in range(column - 1):
        code_number += row + i

    number = 20151125

    for i in range(code_number - 1):
        number *= 252533
        number %= 33554393

    answer = str(number)

    return answer


def main() -> None:
    """Run this day."""
    print("Part 1: " + part_1("day_25.txt"))


if __name__ == "__main__":
    main()
