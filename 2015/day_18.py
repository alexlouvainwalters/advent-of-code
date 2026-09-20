"""This file produces solutions to day 18 of Advent of Code."""


import copy


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    grid = []

    for line in input_data:
        grid.append(list(line.rstrip()))

    next_grid = copy.deepcopy(grid)
    for i in range(100):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                count = 0
                if row != 0:
                    if grid[row - 1][column] == '#':
                        count += 1
                if row != len(grid) - 1:
                    if grid[row + 1][column] == '#':
                        count += 1
                if column != 0:
                    if grid[row][column - 1] == '#':
                        count += 1
                if column != len(grid[row]) - 1:
                    if grid[row][column + 1] == '#':
                        count += 1
                if row != 0 and column != 0:
                    if grid[row - 1][column - 1] == '#':
                        count += 1
                if row != len(grid) - 1 and column != 0:
                    if grid[row + 1][column - 1] == '#':
                        count += 1
                if row != 0 and column != len(grid[row]) - 1:
                    if grid[row - 1][column + 1] == '#':
                        count += 1
                if row != len(grid) - 1 and column != len(grid[row]) - 1:
                    if grid[row + 1][column + 1] == '#':
                        count += 1

                if grid[row][column] == '#' and count != 2 and count != 3:
                    next_grid[row][column] = '.'
                if grid[row][column] == '.' and count == 3:
                    next_grid[row][column] = '#'

        grid = copy.deepcopy(next_grid)

    total = 0
    for row_item in grid:
        for column_item in row_item:
            if column_item == '#':
                total += 1

    answer = str(total)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    grid = []

    for line in input_data:
        grid.append(list(line.rstrip()))

    grid[0][0] = '#'
    grid[0][len(grid[0]) - 1] = '#'
    grid[len(grid) - 1][0] = '#'
    grid[len(grid) - 1][len(grid[0]) - 1] = '#'

    next_grid = copy.deepcopy(grid)
    for i in range(100):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                count = 0
                if row != 0:
                    if grid[row - 1][column] == '#':
                        count += 1
                if row != len(grid) - 1:
                    if grid[row + 1][column] == '#':
                        count += 1
                if column != 0:
                    if grid[row][column - 1] == '#':
                        count += 1
                if column != len(grid[row]) - 1:
                    if grid[row][column + 1] == '#':
                        count += 1
                if row != 0 and column != 0:
                    if grid[row - 1][column - 1] == '#':
                        count += 1
                if row != len(grid) - 1 and column != 0:
                    if grid[row + 1][column - 1] == '#':
                        count += 1
                if row != 0 and column != len(grid[row]) - 1:
                    if grid[row - 1][column + 1] == '#':
                        count += 1
                if row != len(grid) - 1 and column != len(grid[row]) - 1:
                    if grid[row + 1][column + 1] == '#':
                        count += 1

                if grid[row][column] == '#' and count != 2 and count != 3:
                    next_grid[row][column] = '.'
                if grid[row][column] == '.' and count == 3:
                    next_grid[row][column] = '#'

        next_grid[0][0] = '#'
        next_grid[0][len(grid[0]) - 1] = '#'
        next_grid[len(grid) - 1][0] = '#'
        next_grid[len(grid) - 1][len(grid[0]) - 1] = '#'

        grid = copy.deepcopy(next_grid)

    total = 0
    for row_item in grid:
        for column_item in row_item:
            if column_item == '#':
                total += 1

    answer = str(total)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_18.txt"))
    print("Part 2: " + part_2("day_18.txt"))


if __name__ == "__main__":
    main()
