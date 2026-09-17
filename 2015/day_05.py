"""This file produces solutions to day 5 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    count = 0
    for line in input_data:
        nice = True
        vowel_count = 0

        for letter in line:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                vowel_count += 1
        if vowel_count < 3:
            nice = False

        double_letter = False
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                double_letter = True
        if not double_letter:
            nice = False

        for string in ["ab", "cd", "pq", "xy"]:
            if string in line:
                nice = False

        if nice:
            count += 1

    answer = str(count)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    count = 0
    for line in input_data:
        nice = True

        matching = False
        for i in range(len(line) - 1):
            current_pair = line[i:i + 2]
            for j in range(i + 2, len(line) - 1):
                pair = line[j:j + 2]
                if current_pair == pair:
                    matching = True
        if not matching:
            nice = False

        split_letter = False
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                split_letter = True
        if not split_letter:
            nice = False

        if nice:
            count += 1

    answer = str(count)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_05.txt"))
    print("Part 2: " + part_2("day_05.txt"))


if __name__ == "__main__":
    main()
