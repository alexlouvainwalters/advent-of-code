"""This file produces solutions to day 3 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    coords = [0, 0]
    visited_houses = []
    visited_houses.append(coords.copy())

    for line in input_data:
        for i in range(len(line)):
            if line[i] == ">":
                coords[0] += 1
            elif line[i] == "<":
                coords[0] -= 1
            elif line[i] == "^":
                coords[1] += 1
            elif line[i] == "v":
                coords[1] -= 1

            if coords not in visited_houses:
                visited_houses.append(coords.copy())

    answer = str(len(visited_houses))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    coords_1 = [0, 0]
    coords_2 = [0, 0]
    visited_houses = []
    visited_houses.append(coords_1.copy())

    for line in input_data:
        for i in range(0, len(line), 2):
            if line[i] == ">":
                coords_1[0] += 1
            elif line[i] == "<":
                coords_1[0] -= 1
            elif line[i] == "^":
                coords_1[1] += 1
            elif line[i] == "v":
                coords_1[1] -= 1

            if coords_1 not in visited_houses:
                visited_houses.append(coords_1.copy())

            if line[i + 1] == ">":
                coords_2[0] += 1
            elif line[i + 1] == "<":
                coords_2[0] -= 1
            elif line[i + 1] == "^":
                coords_2[1] += 1
            elif line[i + 1] == "v":
                coords_2[1] -= 1

            if coords_2 not in visited_houses:
                visited_houses.append(coords_2.copy())

    answer = str(len(visited_houses))

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_03.txt"))
    print("Part 2: " + part_2("day_03.txt"))


if __name__ == "__main__":
    main()
