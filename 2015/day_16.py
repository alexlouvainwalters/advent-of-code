"""This file produces solutions to day 16 of Advent of Code."""


import re


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    for i in range(len(input_data)):
        line = input_data[i].rstrip()
        line = re.sub(r"Sue \d+: ", "", line)
        possessions = line.split(", ")

        p_dict = {}
        for possession in possessions:
            p_dict[possession.split(": ")[0]] = int(possession.split(": ")[1])

        ticker = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }

        match = True
        for item in ticker.keys():
            if item in p_dict.keys():
                if p_dict[item] != ticker[item]:
                    match = False

        if match:
            answer = str(i + 1)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    for i in range(len(input_data)):
        line = input_data[i].rstrip()
        line = re.sub(r"Sue \d+: ", "", line)
        possessions = line.split(", ")

        p_dict = {}
        for possession in possessions:
            p_dict[possession.split(": ")[0]] = int(possession.split(": ")[1])

        ticker = {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
        }

        match = True
        for item in ticker.keys():
            if item in p_dict.keys():
                if (
                    (
                        (
                            item == "cats"
                            or item == "trees"
                        )
                        and p_dict[item] <= ticker[item]
                    )
                    or (
                        (
                            item == "pomeranians"
                            or item == "goldfish"
                        )
                        and p_dict[item] >= ticker[item]
                    )
                    or (
                        (
                            item != "cats"
                            and item != "trees"
                            and item != "pomeranians"
                            and item != "goldfish"
                        )
                        and ticker[item] != p_dict[item]
                    )
                ):
                    match = False

        if match:
            answer = str(i + 1)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_16.txt"))
    print("Part 2: " + part_2("day_16.txt"))


if __name__ == "__main__":
    main()
