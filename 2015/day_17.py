"""This file produces solutions to day 17 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    fit = 0

    for bitmask in range(1 << len(input_data)):
        combination = []

        for i in range(len(input_data)):
            if bitmask & (1 << i):
                combination.append(input_data[i])

        total = 0
        for size in combination:
            total += int(size)

        if total == 150:
            fit += 1

    answer = str(fit)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    minimum = -1
    ways = 0

    for bitmask in range(1 << len(input_data)):
        combination = []

        for i in range(len(input_data)):
            if bitmask & (1 << i):
                combination.append(input_data[i])

        total = 0
        for size in combination:
            total += int(size)

        if total == 150 and (minimum == -1 or len(combination) < minimum):
            minimum = len(combination)
            ways = 1
        elif total == 150 and len(combination) == minimum:
            ways += 1

    answer = str(ways)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_17.txt"))
    print("Part 2: " + part_2("day_17.txt"))


if __name__ == "__main__":
    main()
