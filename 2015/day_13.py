"""This file produces solutions to day 13 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    table = {}

    for line in input_data:
        line = line.split(" would ")
        line[1] = line[1].split(" happiness units by sitting next to ")
        first_person = line[0]
        second_person = line[1][1].rstrip()[:-1]

        change = line[1][0].split()
        change = line[1][0].split()
        units = int(change[1])
        if change[0] == "lose":
            units *= -1

        if first_person not in table:
            table[first_person] = {}
        if second_person not in table:
            table[second_person] = {}

        if (
            second_person not in table[first_person]
            or first_person not in table[second_person]
        ):
            table[first_person][second_person] = units
            table[second_person][first_person] = units
        else:
            table[first_person][second_person] += units
            table[second_person][first_person] += units

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
        total += table[permutation[0]][permutation[len(permutation) - 1]]
        totals.append(total)

    answer = str(max(totals))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    table = {}

    for line in input_data:
        line = line.split(" would ")
        line[1] = line[1].split(" happiness units by sitting next to ")
        first_person = line[0]
        second_person = line[1][1].rstrip()[:-1]

        change = line[1][0].split()
        change = line[1][0].split()
        units = int(change[1])
        if change[0] == "lose":
            units *= -1

        if first_person not in table:
            table[first_person] = {}
        if second_person not in table:
            table[second_person] = {}

        if (
            second_person not in table[first_person]
            or first_person not in table[second_person]
        ):
            table[first_person][second_person] = units
            table[second_person][first_person] = units
        else:
            table[first_person][second_person] += units
            table[second_person][first_person] += units

    keys = list(table.keys())

    table["X"] = {}
    for key in keys:
        table["X"][key] = 0
        table[key]["X"] = 0

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
        total += table[permutation[0]][permutation[len(permutation) - 1]]
        totals.append(total)

    answer = str(max(totals))

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_13.txt"))
    print("Part 2: " + part_2("day_13.txt"))


if __name__ == "__main__":
    main()
