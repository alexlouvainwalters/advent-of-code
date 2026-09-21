"""This file produces solutions to day 24 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    sum = 0
    for line in input_data:
        sum += int(line.rstrip())

    group_weight = sum / 3

    qes = []

    for size in range(1, len(input_data) + 1):

        states = [[0, 0, []]]

        while states:
            start, weight, numbers = states.pop()

            if weight == group_weight:
                product = 1
                for number in numbers:
                    product *= number
                qes.append(product)

            if weight >= group_weight or len(numbers) >= size:
                continue

            for i in range(start, len(input_data)):
                next = int(input_data[i].rstrip())

                if weight + next <= group_weight:
                    states.append([
                        i + 1,
                        weight + int(next),
                        numbers + [next]
                    ])

        if qes:
            break

    answer = str(min(qes))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    sum = 0
    for line in input_data:
        sum += int(line.rstrip())

    group_weight = sum / 4

    qes = []

    for size in range(1, len(input_data) + 1):

        states = [[0, 0, []]]

        while states:
            start, weight, numbers = states.pop()

            if weight == group_weight:
                product = 1
                for number in numbers:
                    product *= number
                qes.append(product)

            if weight >= group_weight or len(numbers) >= size:
                continue

            for i in range(start, len(input_data)):
                next = int(input_data[i].rstrip())

                if weight + next <= group_weight:
                    states.append([
                        i + 1,
                        weight + int(next),
                        numbers + [next]
                    ])

        if qes:
            break

    answer = str(min(qes))

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_24.txt"))
    print("Part 2: " + part_2("day_24.txt"))


if __name__ == "__main__":
    main()
