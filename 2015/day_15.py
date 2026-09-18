"""This file produces solutions to day 15 of Advent of Code."""


import re


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    capacity = []
    durability = []
    flavor = []
    texture = []
    calories = []

    for i in range(len(input_data)):
        values = re.findall(r"-?\d+", input_data[i])
        capacity.append(int(values[0]))
        durability.append(int(values[1]))
        flavor.append(int(values[2]))
        texture.append(int(values[3]))
        calories.append(int(values[4]))

    products = []

    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                m = 100 - i - j - k

                capacity_value = (
                    i * capacity[0]
                    + j * capacity[1]
                    + k * capacity[2]
                    + m * capacity[3]
                )
                durability_value = (
                    i * durability[0]
                    + j * durability[1]
                    + k * durability[2]
                    + m * durability[3]
                )
                flavor_value = (
                    i * flavor[0]
                    + j * flavor[1]
                    + k * flavor[2]
                    + m * flavor[3]
                )
                texture_value = (
                    i * texture[0]
                    + j * texture[1]
                    + k * texture[2]
                    + m * texture[3]
                )

                if (
                    capacity_value <= 0
                    or durability_value <= 0
                    or flavor_value <= 0
                    or texture_value <= 0
                ):
                    product = 0
                else:
                    product = (
                        capacity_value
                        * durability_value
                        * flavor_value
                        * texture_value
                    )

                products.append(product)

    answer = str(max(products))

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    capacity = []
    durability = []
    flavor = []
    texture = []
    calories = []

    for i in range(len(input_data)):
        values = re.findall(r"-?\d+", input_data[i])
        capacity.append(int(values[0]))
        durability.append(int(values[1]))
        flavor.append(int(values[2]))
        texture.append(int(values[3]))
        calories.append(int(values[4]))

    products = []

    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                m = 100 - i - j - k

                capacity_value = (
                    i * capacity[0]
                    + j * capacity[1]
                    + k * capacity[2]
                    + m * capacity[3]
                )
                durability_value = (
                    i * durability[0]
                    + j * durability[1]
                    + k * durability[2]
                    + m * durability[3]
                )
                flavor_value = (
                    i * flavor[0]
                    + j * flavor[1]
                    + k * flavor[2]
                    + m * flavor[3]
                )
                texture_value = (
                    i * texture[0]
                    + j * texture[1]
                    + k * texture[2]
                    + m * texture[3]
                )
                calories_value = (
                    i * calories[0]
                    + j * calories[1]
                    + k * calories[2]
                    + m * calories[3]
                )

                if (
                    capacity_value <= 0
                    or durability_value <= 0
                    or flavor_value <= 0
                    or texture_value <= 0
                ):
                    product = 0
                else:
                    product = (
                        capacity_value
                        * durability_value
                        * flavor_value
                        * texture_value
                    )

                if calories_value == 500:
                    products.append(product)

    answer = str(max(products))

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_15.txt"))
    print("Part 2: " + part_2("day_15.txt"))


if __name__ == "__main__":
    main()
