import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    player_list: list = ['Alice',
                         'bob',
                         'Charlie',
                         'dylan',
                         'Emma',
                         'Gregory',
                         'john',
                         'kevin',
                         'Liam']

    print(f"Initial list of players: {player_list}")

    capitalized_list: list = [x.capitalize() for x in player_list]
    print(f"New list with all names capitalized: {capitalized_list}")

    only_cap: list = [x for x in player_list if x[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

    scores: dict = {x: random.randint(1, 1000) for x in capitalized_list}
    print(f"\nScore dict: {scores}")

    total_score: int = sum(scores[name] for name in scores)
    average: float = total_score / len(scores)
    highscores = {name: scores[name] for name in scores if
                  scores[name] > average}
    print(f"Score average is {average:.2f}")
    print(f"High scores: {highscores}")


if __name__ == "__main__":
    main()
