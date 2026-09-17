"""This file produces solutions to day 10 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    number = input_data
    next = ""

    for i in range(40):
        previous = None
        count = 1
        for char in str(number):
            if previous is None:
                previous = char
            elif previous != char:
                next += str(count)
                next += previous
                previous = char
                count = 1
            else:
                count += 1
        next += str(count)
        next += previous
        number = next
        next = ""

    answer = str(len(number))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    number = input_data
    next = ""

    for i in range(50):
        previous = None
        count = 1
        for char in str(number):
            if previous is None:
                previous = char
            elif previous != char:
                next += str(count)
                next += previous
                previous = char
                count = 1
            else:
                count += 1
        next += str(count)
        next += previous
        number = next
        next = ""

    answer = str(len(number))

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_10.txt"))
    print("Part 2: " + part_2("day_10.txt"))


if __name__ == "__main__":
    main()
