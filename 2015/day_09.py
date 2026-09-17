"""This file produces solutions to day 9 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    table = {}

    for line in input_data:
        line = line.split(" = ")
        line[0] = line[0].split(" to ")
        if line[0][0] not in table:
            table[line[0][0]] = {}
        if line[0][1] not in table:
            table[line[0][1]] = {}
        table[line[0][0]][line[0][1]] = int(line[1].rstrip())
        table[line[0][1]][line[0][0]] = int(line[1].rstrip())

    keys = list(table.keys())
    permutations = [[]]

    for key in keys:
        new_permutations = []
        for p in permutations:
            for i in range(len(p) + 1):
                permutation = p.copy()
                permutation.insert(i, key)
                new_permutations.append(permutation)
        permutations = new_permutations

    totals = []

    for permutation in permutations:
        total = 0
        for i in range(len(permutation) - 1):
            total += table[permutation[i]][permutation[i + 1]]
        totals.append(total)

    answer = str(min(totals))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    table = {}

    for line in input_data:
        line = line.split(" = ")
        line[0] = line[0].split(" to ")
        if line[0][0] not in table:
            table[line[0][0]] = {}
        if line[0][1] not in table:
            table[line[0][1]] = {}
        table[line[0][0]][line[0][1]] = int(line[1].rstrip())
        table[line[0][1]][line[0][0]] = int(line[1].rstrip())

    keys = list(table.keys())
    permutations = [[]]

    for key in keys:
        new_permutations = []
        for p in permutations:
            for i in range(len(p) + 1):
                permutation = p.copy()
                permutation.insert(i, key)
                new_permutations.append(permutation)
        permutations = new_permutations

    totals = []

    for permutation in permutations:
        total = 0
        for i in range(len(permutation) - 1):
            total += table[permutation[i]][permutation[i + 1]]
        totals.append(total)

    answer = str(max(totals))

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_09.txt"))
    print("Part 2: " + part_2("day_09.txt"))


if __name__ == "__main__":
    main()
