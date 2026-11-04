class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.oldness = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.oldness} days old")

    def grow(self, growth: float = 0.8) -> None:
        self.height += growth

    def age(self) -> None:
        self.oldness += 1


def main() -> None:
    r = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    r.show()
    growth = r.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        r.grow(0.8)
        r.age()
        r.show()
    growth = r.height - growth
    print(f"Growth this week: {growth:.1f}cm")


if __name__ == "__main__":
    main()
