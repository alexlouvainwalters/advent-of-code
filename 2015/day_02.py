"""This file produces solutions to day 2 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    total = 0
    for line in input_data:
        dimensions = list(map(int, line.split("x")))
        sides = []
        sides.append(dimensions[0] * dimensions[1])
        sides.append(dimensions[0] * dimensions[2])
        sides.append(dimensions[1] * dimensions[2])
        for side in sides:
            total += 2 * side
        total += min(sides)

    answer = str(total)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    total = 0
    for line in input_data:
        dimensions = list(map(int, line.split("x")))
        total += 2 * (dimensions[0] + dimensions[1] + dimensions[2])
        total -= 2 * max(dimensions)
        total += dimensions[0] * dimensions[1] * dimensions[2]

    answer = str(total)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_02.txt"))
    print("Part 2: " + part_2("day_02.txt"))


if __name__ == "__main__":
    main()
