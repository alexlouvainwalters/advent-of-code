"""This file produces solutions to day 21 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    boss_stats = []
    boss_stats.append(int(input_data[0].rstrip().split(": ")[1]))
    boss_stats.append(int(input_data[1].rstrip().split(": ")[1]))
    boss_stats.append(int(input_data[2].rstrip().split(": ")[1]))

    weapons = [
        [8, 4, 0],
        [10, 5, 0],
        [25, 6, 0],
        [40, 7, 0],
        [74, 8, 0]
    ]

    armor = [
        [0, 0, 0],
        [13, 0, 1],
        [31, 0, 2],
        [53, 0, 3],
        [75, 0, 4],
        [102, 0, 5]
    ]

    rings_raw = [
        [0, 0, 0],
        [25, 1, 0],
        [50, 2, 0],
        [100, 3, 0],
        [20, 0, 1],
        [40, 0, 2],
        [80, 0, 3]
    ]

    rings = [[0, 0, 0]]
    for i in range(len(rings_raw)):
        for j in range(i + 1, len(rings_raw)):
            rings.append([
                rings_raw[i][0] + rings_raw[j][0],
                rings_raw[i][1] + rings_raw[j][1],
                rings_raw[i][2] + rings_raw[j][2]
            ])

    stats = []
    for x in weapons:
        for y in armor:
            for z in rings:
                stats.append([
                    100,
                    x[1] + y[1] + z[1],
                    x[2] + y[2] + z[2],
                    x[0] + y[0] + z[0]
                ])

    minimum = -1

    for player_stats in stats:
        player_health = player_stats[0]
        boss_health = boss_stats[0]
        player_damage = max([player_stats[1] - boss_stats[2], 1])
        boss_damage = max([boss_stats[1] - player_stats[2], 1])

        while True:
            boss_health -= player_damage
            if boss_health <= 0:
                if player_stats[3] < minimum or minimum == -1:
                    minimum = player_stats[3]
                break
            player_health -= boss_damage
            if player_health <= 0:
                break

    answer = str(minimum)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    boss_stats = []
    boss_stats.append(int(input_data[0].rstrip().split(": ")[1]))
    boss_stats.append(int(input_data[1].rstrip().split(": ")[1]))
    boss_stats.append(int(input_data[2].rstrip().split(": ")[1]))

    weapons = [
        [8, 4, 0],
        [10, 5, 0],
        [25, 6, 0],
        [40, 7, 0],
        [74, 8, 0]
    ]

    armor = [
        [0, 0, 0],
        [13, 0, 1],
        [31, 0, 2],
        [53, 0, 3],
        [75, 0, 4],
        [102, 0, 5]
    ]

    rings_raw = [
        [0, 0, 0],
        [25, 1, 0],
        [50, 2, 0],
        [100, 3, 0],
        [20, 0, 1],
        [40, 0, 2],
        [80, 0, 3]
    ]

    rings = [[0, 0, 0]]
    for i in range(len(rings_raw)):
        for j in range(i + 1, len(rings_raw)):
            rings.append([
                rings_raw[i][0] + rings_raw[j][0],
                rings_raw[i][1] + rings_raw[j][1],
                rings_raw[i][2] + rings_raw[j][2]
            ])

    stats = []
    for x in weapons:
        for y in armor:
            for z in rings:
                stats.append([
                    100,
                    x[1] + y[1] + z[1],
                    x[2] + y[2] + z[2],
                    x[0] + y[0] + z[0]
                ])

    maximum = -1

    for player_stats in stats:
        player_health = player_stats[0]
        boss_health = boss_stats[0]
        player_damage = max([player_stats[1] - boss_stats[2], 1])
        boss_damage = max([boss_stats[1] - player_stats[2], 1])

        while True:
            boss_health -= player_damage
            if boss_health <= 0:
                break
            player_health -= boss_damage
            if player_health <= 0:
                if player_stats[3] > maximum:
                    maximum = player_stats[3]
                break

    answer = str(maximum)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_21.txt"))
    print("Part 2: " + part_2("day_21.txt"))


if __name__ == "__main__":
    main()
