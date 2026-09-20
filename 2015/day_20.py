"""This file produces solutions to day 20 of Advent of Code."""


import math


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    total = 0
    house = 0

    while total < int(input_data):
        total = 0
        house += 1

        for i in range(math.isqrt(house), 0, -1):
            if house % i == 0:
                total += 10 * i
                if i ** 2 != house:
                    total += 10 * (house // i)

    answer = str(house)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    total = 0
    house = 0

    while total < int(input_data):
        total = 0
        house += 1

        for i in range(math.isqrt(house), 0, -1):
            if house % i == 0:
                if 50 >= house // i:
                    total += 11 * i
                if i ** 2 != house:
                    if 50 >= i:
                        total += 11 * (house // i)

    answer = str(house)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_20.txt"))
    print("Part 2: " + part_2("day_20.txt"))


if __name__ == "__main__":
    main()
