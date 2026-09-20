"""This file produces solutions to day 19 of Advent of Code."""


import re


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    replacements = []

    for line in input_data:
        if " => " in line:
            replacements.append(line.rstrip().split(" => "))
        elif line.rstrip() != "":
            chemical = line.rstrip()

    molecules = []

    for replacement in replacements:
        for found in re.finditer(re.escape(replacement[0]), chemical):
            new = (
                chemical[:found.start()]
                + replacement[1]
                + chemical[found.end():]
            )
            if new not in molecules:
                molecules.append(new)

    answer = str(len(molecules))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    replacements = []

    for line in input_data:
        if " => " in line:
            replacements.append(line.rstrip().split(" => "))
        elif line.rstrip() != "":
            chemical = line.rstrip()

    replacements.sort(key=lambda item: len(item[1]), reverse=True)

    steps = 0
    match = False
    chemicals = [chemical]

    while not match:
        steps += 1
        for chemical in chemicals:
            for replacement in replacements:
                found = re.search(re.escape(replacement[1]), chemical)
                if found:
                    new = (
                        chemical[:found.start()]
                        + replacement[0]
                        + chemical[found.end():]
                    )

                    if new == 'e':
                        match = True

                    chemicals = [new]
                    break

            if match:
                break

    answer = str(steps)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_19.txt"))
    print("Part 2: " + part_2("day_19.txt"))


if __name__ == "__main__":
    main()
