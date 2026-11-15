import random
from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "grab", "use", "eat", "sleep", "move", "climb", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(PLAYERS)
        action: str = random.choice(ACTIONS)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str],
                                                              None, None]:
    while events:
        random_i: int = random.randint(0, len(events) - 1)
        event: tuple[str, str] = events.pop(random_i)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generate_event = gen_event()
    for i in range(1000):
        name, action = next(generate_event)
        print(f"Event {i}: Player {name} did action {action}")

    events = [next(generate_event) for x in range(10)]
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        name, action = event
        print(f"Got event from list: ('{name}', '{action}')")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
