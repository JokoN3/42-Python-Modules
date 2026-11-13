import random


ALL_ACHIEVEMENTS = [
    'Crafting Genius',
    'World Savior',
    'Master Explorer',
    'Collector Supreme',
    'Untouchable',
    'Boss Slayer',
    'Strategist',
    'Speed Runner',
    'Survivor',
    'Treasure Hunter',
    'Unstoppable',
    'Hidden Path Finder',
    'First Steps',
    'Sharp Mind'
]


def gen_player_achievements() -> set:
    picked: list = random.sample(ALL_ACHIEVEMENTS, random.randint(3, 6))
    return set(picked)


def print_player(player: tuple) -> None:
    print(f"Player {player[0]}: {player[1]}")


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    a_set: set = gen_player_achievements()
    alice: tuple = ("Alice", a_set)
    print_player(alice)

    b_set: set = gen_player_achievements()
    bob: tuple = ("Bob", b_set)
    print_player(bob)

    c_set: set = gen_player_achievements()
    charlie: tuple = ("Charlie", c_set)
    print_player(charlie)

    d_set: set = gen_player_achievements()
    dylan: tuple = ("Dylan", d_set)
    print_player(dylan)

    all_achievements_set: set = set(ALL_ACHIEVEMENTS)

    all_distinct: set = a_set | b_set | c_set | d_set
    print(f"\nAll distinct achievements: {all_distinct}")

    common: set = a_set & b_set & c_set & d_set
    print(f"\nCommon achievements: {common}\n")

    only_alice: set = a_set.difference(b_set, c_set, d_set)
    print(f"Only Alice has: {only_alice}")
    only_bob: set = b_set.difference(a_set, c_set, d_set)
    print(f"Only Bob has: {only_bob}")
    only_charlie: set = c_set.difference(a_set, b_set, d_set)
    print(f"Only Charlie has: {only_charlie}")
    only_dylan: set = d_set.difference(a_set, b_set, c_set)
    print(f"Only Dylan has: {only_dylan}")

    print(f"\nAlice is missing: {all_achievements_set - a_set}")
    print(f"Bob is missing: {all_achievements_set - b_set}")
    print(f"Charlie is missing: {all_achievements_set - c_set}")
    print(f"Dylan is missing: {all_achievements_set - d_set}")


if __name__ == "__main__":
    main()
