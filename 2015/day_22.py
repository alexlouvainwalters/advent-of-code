"""This file produces solutions to day 22 of Advent of Code."""


def part_1(input_file: str) -> str:
    """Return the answer to part 1."""
    answer = ""

    with open(input_file) as file:
        input_data = file.readlines()

    boss_stats = []
    boss_stats.append(int(input_data[0].rstrip().split(": ")[1]))
    boss_stats.append(int(input_data[1].rstrip().split(": ")[1]))

    spells = [53, 73, 113, 173, 229]
    minimum = -1

    states = [[50, 500, boss_stats[0], 0, 0, 0, 0]]
    while states:
        (
            player_health,
            player_mana,
            boss_health,
            shield_timer,
            poison_timer,
            recharge_timer,
            spent_mana
        ) = states.pop()

        if spent_mana >= minimum and minimum != -1:
            continue

        for spell_index in range(len(spells)):
            new_player_health = player_health
            new_player_mana = player_mana
            new_boss_health = boss_health
            new_shield_timer = shield_timer
            new_poison_timer = poison_timer
            new_recharge_timer = recharge_timer

            if new_shield_timer > 0:
                new_shield_timer -= 1
            if new_poison_timer > 0:
                new_boss_health -= 3
                new_poison_timer -= 1
            if new_recharge_timer > 0:
                new_player_mana += 101
                new_recharge_timer -= 1

            if new_boss_health <= 0:
                minimum = min(minimum, spent_mana)
                if minimum == -1:
                    minimum = spent_mana
                continue

            if (
                new_player_mana < spells[spell_index]
                or (spell_index == 2 and new_shield_timer > 0)
                or (spell_index == 3 and new_poison_timer > 0)
                or (spell_index == 4 and new_recharge_timer > 0)
            ):
                continue

            new_player_mana -= spells[spell_index]

            if spell_index == 0:
                new_boss_health -= 4
            elif spell_index == 1:
                new_boss_health -= 2
                new_player_health += 2
            elif spell_index == 2:
                new_shield_timer = 6
            elif spell_index == 3:
                new_poison_timer = 6
            elif spell_index == 4:
                new_recharge_timer = 5

            new_spent_mana = spent_mana + spells[spell_index]
            if new_boss_health <= 0:
                minimum = min(minimum, new_spent_mana)
                if minimum == -1:
                    minimum = new_spent_mana
                continue

            if new_shield_timer > 0:
                armour = 7
            else:
                armour = 0

            if new_shield_timer > 0:
                new_shield_timer -= 1
            if new_poison_timer > 0:
                new_boss_health -= 3
                new_poison_timer -= 1
            if new_recharge_timer > 0:
                new_player_mana += 101
                new_recharge_timer -= 1

            if new_boss_health <= 0:
                minimum = min(minimum, new_spent_mana)
                if minimum == -1:
                    minimum = new_spent_mana
                continue

            new_player_health -= max(1, boss_stats[1] - armour)

            if new_player_health <= 0:
                continue

            states.append([
                new_player_health,
                new_player_mana,
                new_boss_health,
                new_shield_timer,
                new_poison_timer,
                new_recharge_timer,
                new_spent_mana
            ])

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

    spells = [53, 73, 113, 173, 229]
    minimum = -1

    states = [[50, 500, boss_stats[0], 0, 0, 0, 0]]
    while states:
        (
            player_health,
            player_mana,
            boss_health,
            shield_timer,
            poison_timer,
            recharge_timer,
            spent_mana
        ) = states.pop()

        if spent_mana >= minimum and minimum != -1:
            continue

        for spell_index in range(len(spells)):
            new_player_health = player_health - 1
            new_player_mana = player_mana
            new_boss_health = boss_health
            new_shield_timer = shield_timer
            new_poison_timer = poison_timer
            new_recharge_timer = recharge_timer

            if new_shield_timer > 0:
                new_shield_timer -= 1
            if new_poison_timer > 0:
                new_boss_health -= 3
                new_poison_timer -= 1
            if new_recharge_timer > 0:
                new_player_mana += 101
                new_recharge_timer -= 1

            if new_boss_health <= 0:
                minimum = min(minimum, spent_mana)
                if minimum == -1:
                    minimum = spent_mana
                continue

            if new_player_health <= 0:
                continue

            if (
                new_player_mana < spells[spell_index]
                or (spell_index == 2 and new_shield_timer > 0)
                or (spell_index == 3 and new_poison_timer > 0)
                or (spell_index == 4 and new_recharge_timer > 0)
            ):
                continue

            new_player_mana -= spells[spell_index]

            if spell_index == 0:
                new_boss_health -= 4
            elif spell_index == 1:
                new_boss_health -= 2
                new_player_health += 2
            elif spell_index == 2:
                new_shield_timer = 6
            elif spell_index == 3:
                new_poison_timer = 6
            elif spell_index == 4:
                new_recharge_timer = 5

            new_spent_mana = spent_mana + spells[spell_index]
            if new_boss_health <= 0:
                minimum = min(minimum, new_spent_mana)
                if minimum == -1:
                    minimum = new_spent_mana
                continue

            if new_shield_timer > 0:
                armour = 7
            else:
                armour = 0

            if new_shield_timer > 0:
                new_shield_timer -= 1
            if new_poison_timer > 0:
                new_boss_health -= 3
                new_poison_timer -= 1
            if new_recharge_timer > 0:
                new_player_mana += 101
                new_recharge_timer -= 1

            if new_boss_health <= 0:
                minimum = min(minimum, new_spent_mana)
                if minimum == -1:
                    minimum = new_spent_mana
                continue

            new_player_health -= max(1, boss_stats[1] - armour)

            if new_player_health <= 0:
                continue

            states.append([
                new_player_health,
                new_player_mana,
                new_boss_health,
                new_shield_timer,
                new_poison_timer,
                new_recharge_timer,
                new_spent_mana
            ])

    answer = str(minimum)

    return answer


def main() -> None:
    """Run both parts of this day."""
    print("Part 1: " + part_1("day_22.txt"))
    print("Part 2: " + part_2("day_22.txt"))


if __name__ == "__main__":
    main()
