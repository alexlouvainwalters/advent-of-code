"""This file produces solutions to day 1 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    up_count = input_data.count("(")
    down_count = input_data.count(")")

    answer = str(up_count - down_count)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    for i in range(len(input_data)):
        up_count = input_data[:i].count("(")
        down_count = input_data[:i].count(")")

        if (up_count < down_count):
            answer = str(i)
            break

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_01.txt"))
    print("Part 2: " + part_2("day_01.txt"))


if __name__ == "__main__":
    main()
