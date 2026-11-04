class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def grow_called(self) -> None:
            self._grow_calls += 1

        def age_called(self) -> None:
            self._age_calls += 1

        def show_called(self) -> None:
            self._show_calls += 1

        def display_stats(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")


    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self.stats = self.Statistics()
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
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if (self.has_bloomed):
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.has_bloomed = True


class Vegetable(Plant):
    def __init__(self, name: str, height: float, 
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutri_val = 0

    def grow_and_age(self, days_to_age: int) -> None:
        for i in range(days_to_age):
            super().age()
            super().grow(2.1)
            self.nutri_val += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutri_val}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_dia = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_dia}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}", end="")
        print(f"cm long and {self.trunk_dia}cm wide.")

def main() -> None:
    rose = Flower("Rose", 5, 12, "red")
    rose.show()
    rose.stats.display_stats()

if __name__ == "__main__":
    main()