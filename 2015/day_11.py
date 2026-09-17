"""This file produces solutions to day 11 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    password = list(input_data)
    first = False
    second = False
    third = False

    while not first or not second or not third:
        first = False
        second = False
        third = False

        for i in range(len(password) - 2):
            if (
                ord(password[i]) == ord(password[i + 1]) - 1
                and ord(password[i + 1]) == ord(password[i + 2]) - 1
            ):
                first = True

        if 'i' not in password and 'o' not in password and 'l' not in password:
            second = True

        count = 0
        for i in range(len(password) - 1):
            if i != 0 and password[i - 1] == password[i]:
                continue
            if password[i] == password[i + 1]:
                count += 1
        if count >= 2:
            third = True

        if not first or not second or not third:
            for i in range(len(password) - 1, -1, -1):
                if password[i] == 'z':
                    password[i] = 'a'
                else:
                    password[i] = chr(ord(password[i]) + 1)
                    break

    answer = ''.join(password)

    return answer


def part_2(input_file: str) -> str:
    """Return the answer to part 2."""
    answer = ""

    with open(input_file) as file:
        input_data = file.read()

    password = list(input_data)
    first = False
    second = False
    third = False
    new_passwords = 0

    while not first or not second or not third or new_passwords < 2:
        first = False
        second = False
        third = False

        for i in range(len(password) - 2):
            if (
                ord(password[i]) == ord(password[i + 1]) - 1
                and ord(password[i + 1]) == ord(password[i + 2]) - 1
            ):
                first = True

        if 'i' not in password and 'o' not in password and 'l' not in password:
            second = True

        count = 0
        for i in range(len(password) - 1):
            if i != 0 and password[i - 1] == password[i]:
                continue
            if password[i] == password[i + 1]:
                count += 1
        if count >= 2:
            third = True

        if first and second and third:
            new_passwords += 1

        if not first or not second or not third or new_passwords < 2:
            for i in range(len(password) - 1, -1, -1):
                if password[i] == 'z':
                    password[i] = 'a'
                else:
                    password[i] = chr(ord(password[i]) + 1)
                    break

    answer = ''.join(password)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_11.txt"))
    print("Part 2: " + part_2("day_11.txt"))


if __name__ == "__main__":
    main()
