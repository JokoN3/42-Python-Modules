import sys


def process_args(argv: list[str]) -> list[int]:
    processed_args: list[int] = []
    for arg in argv:
        try:
            processed_args.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    return processed_args


def main() -> None:
    print("=== Player Score Analytics ===")
    processed_args: list[int] = process_args(sys.argv[1:])

    if not processed_args:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    print(f"Scores processed: {processed_args}")
    print(f"Total players: {len(processed_args)}")
    print(f"Total score: {sum(processed_args)}")
    print(f"Average score: {sum(processed_args) / len(processed_args)}")
    print(f"High score: {max(processed_args)}")
    print(f"Low score: {min(processed_args)}")
    print(f"Score range: {max(processed_args) - min(processed_args)}")


if __name__ == "__main__":
    main()
