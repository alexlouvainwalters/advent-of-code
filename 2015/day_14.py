"""This file produces solutions to day 14 of Advent of Code."""


import re


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    speeds = []
    times = []
    rests = []
    distances = []

    for i in range(len(input_data)):
        values = re.findall(r"\d+", input_data[i])
        speeds.append(int(values[0]))
        times.append(int(values[1]))
        rests.append(int(values[2]))
        distances.append(0)

    temp_times = times.copy()
    temp_rests = rests.copy()

    count = 2503
    while count > 0:
        count -= 1

        for i in range(len(input_data)):
            if temp_times[i] > 0:
                temp_times[i] -= 1
                distances[i] += speeds[i]

            elif temp_times[i] == 0 and temp_rests[i] > 0:
                temp_rests[i] -= 1

            else:
                temp_times[i] = times[i] - 1
                temp_rests[i] = rests[i]
                distances[i] += speeds[i]

    answer = str(max(distances))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    speeds = []
    times = []
    rests = []
    distances = []
    points = []

    for i in range(len(input_data)):
        values = re.findall(r"\d+", input_data[i])
        speeds.append(int(values[0]))
        times.append(int(values[1]))
        rests.append(int(values[2]))
        distances.append(0)
        points.append(0)

    temp_times = times.copy()
    temp_rests = rests.copy()

    count = 2503
    while count > 0:
        count -= 1

        for i in range(len(input_data)):
            if temp_times[i] > 0:
                temp_times[i] -= 1
                distances[i] += speeds[i]

            elif temp_times[i] == 0 and temp_rests[i] > 0:
                temp_rests[i] -= 1

            else:
                temp_times[i] = times[i] - 1
                temp_rests[i] = rests[i]
                distances[i] += speeds[i]

        lead = max(distances)
        for i in range(len(input_data)):
            if lead == distances[i]:
                points[i] += 1

    answer = str(max(points))

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_14.txt"))
    print("Part 2: " + part_2("day_14.txt"))


if __name__ == "__main__":
    main()
