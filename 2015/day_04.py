"""This file produces solutions to day 4 of Advent of Code."""


import hashlib


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    count = 1
    while True:
        full_key = input_data + str(count)
        result = hashlib.md5(full_key.encode())
        if result.hexdigest()[:5] == "00000":
            answer = str(count)
            break
        count += 1

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    count = 1
    while True:
        full_key = input_data + str(count)
        result = hashlib.md5(full_key.encode())
        if result.hexdigest()[:6] == "000000":
            answer = str(count)
            break
        count += 1

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_04.txt"))
    print("Part 2: " + part_2("day_04.txt"))


if __name__ == "__main__":
    main()
