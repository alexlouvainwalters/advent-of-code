"""This file produces solutions to day 6 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    lights = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row.append(False)
        lights.append(row)

    for line in input_data:
        if line[:6] != "toggle":
            line = line[:4] + line[5:]

        line = line.split()
        line[1] = line[1].split(",")
        line[3] = line[3].split(",")

        for i in range(int(line[1][0]), int(line[3][0]) + 1):
            for j in range(int(line[1][1]), int(line[3][1]) + 1):
                if line[0] == "turnon":
                    lights[i][j] = True
                elif line[0] == "turnoff":
                    lights[i][j] = False
                elif line[0] == "toggle":
                    if lights[i][j]:
                        lights[i][j] = False
                    else:
                        lights[i][j] = True

    count = 0
    for i in range(1000):
        for j in range(1000):
            if lights[i][j]:
                count += 1

    answer = str(count)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    lights = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row.append(0)
        lights.append(row)

    for line in input_data:
        if line[:6] != "toggle":
            line = line[:4] + line[5:]

        line = line.split()
        line[1] = line[1].split(",")
        line[3] = line[3].split(",")

        for i in range(int(line[1][0]), int(line[3][0]) + 1):
            for j in range(int(line[1][1]), int(line[3][1]) + 1):
                if line[0] == "turnon":
                    lights[i][j] += 1
                elif line[0] == "turnoff" and lights[i][j] != 0:
                    lights[i][j] -= 1
                elif line[0] == "toggle":
                    lights[i][j] += 2

    brightness = 0
    for i in range(1000):
        for j in range(1000):
            brightness += lights[i][j]

    answer = str(brightness)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_06.txt"))
    print("Part 2: " + part_2("day_06.txt"))


if __name__ == "__main__":
    main()
