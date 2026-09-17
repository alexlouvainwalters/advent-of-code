"""This file produces solutions to day 8 of Advent of Code."""


import re


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    total_string_length = 0
    total_memory_length = 0

    for line in input_data:
        line = line.rstrip()

        string_length = len(line)

        line = line[1:-1]
        line = re.sub(r"\\\\", "?", line)
        line = re.sub(r"\\\"", "?", line)
        line = re.sub(r"\\x[0-9a-fA-F]{2}", "?", line)

        memory_length = len(line)

        total_string_length += string_length
        total_memory_length += memory_length

    answer = str(total_string_length - total_memory_length)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    total_string_length = 0
    total_memory_length = 0

    for line in input_data:
        line = line.rstrip()

        memory_length = len(line)

        line = re.sub(r"\\", r"\\\\", line)
        line = re.sub(r"\"", "\\\"", line)
        line = "\"" + line + "\""

        string_length = len(line)

        total_string_length += string_length
        total_memory_length += memory_length

    answer = str(total_string_length - total_memory_length)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_08.txt"))
    print("Part 2: " + part_2("day_08.txt"))


if __name__ == "__main__":
    main()
