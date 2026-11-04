class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self, growth: float = 0.8) -> None:
        self.set_height(self._height + growth)

    def age(self) -> None:
        self.set_age(self._age + 1)

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height


def main() -> None:
    print("=== Garden Security System ===")
    r = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    r.show()
    print()
    r.set_height(25)
    r.set_age(30)
    print()
    r.set_height(-1)
    r.set_age(-1)
    print()
    print("Current state: ", end="")
    r.show()


if __name__ == "__main__":
    main()
