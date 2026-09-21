"""This file produces solutions to day 23 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    a, b = 0, 0
    index = 0

    while index < len(input_data):
        instruction = input_data[index].rstrip().split()

        if instruction[0] == "hlf":
            if instruction[1] == 'a':
                a /= 2
            elif instruction[1] == 'b':
                b /= 2
            index += 1
        elif instruction[0] == "tpl":
            if instruction[1] == 'a':
                a *= 3
            elif instruction[1] == 'b':
                b *= 3
            index += 1
        elif instruction[0] == "inc":
            if instruction[1] == 'a':
                a += 1
            elif instruction[1] == 'b':
                b += 1
            index += 1
        elif instruction[0] == "jmp":
            if instruction[1][0] == '+':
                index += int(instruction[1][1:])
            elif instruction[1][0] == '-':
                index -= int(instruction[1][1:])
        elif instruction[0] == "jie":
            if (
                (instruction[1][0] == 'a' and a % 2 == 0)
                or (instruction[1][0] == 'b' and b % 2 == 0)
            ):
                if instruction[2][0] == '+':
                    index += int(instruction[2][1:])
                elif instruction[2][0] == '-':
                    index -= int(instruction[2][1:])
            else:
                index += 1
        elif instruction[0] == "jio":
            if (
                (instruction[1][0] == 'a' and a == 1)
                or (instruction[1][0] == 'b' and b == 1)
            ):
                if instruction[2][0] == '+':
                    index += int(instruction[2][1:])
                elif instruction[2][0] == '-':
                    index -= int(instruction[2][1:])
            else:
                index += 1

    answer = str(b)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    a, b = 1, 0
    index = 0

    while index < len(input_data):
        instruction = input_data[index].rstrip().split()

        if instruction[0] == "hlf":
            if instruction[1] == 'a':
                a /= 2
            elif instruction[1] == 'b':
                b /= 2
            index += 1
        elif instruction[0] == "tpl":
            if instruction[1] == 'a':
                a *= 3
            elif instruction[1] == 'b':
                b *= 3
            index += 1
        elif instruction[0] == "inc":
            if instruction[1] == 'a':
                a += 1
            elif instruction[1] == 'b':
                b += 1
            index += 1
        elif instruction[0] == "jmp":
            if instruction[1][0] == '+':
                index += int(instruction[1][1:])
            elif instruction[1][0] == '-':
                index -= int(instruction[1][1:])
        elif instruction[0] == "jie":
            if (
                (instruction[1][0] == 'a' and a % 2 == 0)
                or (instruction[1][0] == 'b' and b % 2 == 0)
            ):
                if instruction[2][0] == '+':
                    index += int(instruction[2][1:])
                elif instruction[2][0] == '-':
                    index -= int(instruction[2][1:])
            else:
                index += 1
        elif instruction[0] == "jio":
            if (
                (instruction[1][0] == 'a' and a == 1)
                or (instruction[1][0] == 'b' and b == 1)
            ):
                if instruction[2][0] == '+':
                    index += int(instruction[2][1:])
                elif instruction[2][0] == '-':
                    index -= int(instruction[2][1:])
            else:
                index += 1

    answer = str(b)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_23.txt"))
    print("Part 2: " + part_2("day_23.txt"))


if __name__ == "__main__":
    main()
