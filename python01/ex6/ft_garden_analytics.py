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

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, "
                  f"{self._show_calls} show")

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
        self.stats.show_called()

    def grow(self, growth: float = 0.8) -> None:
        self.set_height(self._height + growth)
        self.stats.grow_called()

    def age(self, to_age: int = 1) -> None:
        self.set_age(self._age + to_age)
        self.stats.age_called()

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

    @staticmethod
    def is_older_than_year(age_to_check: int) -> bool:
        return age_to_check > 365

    @classmethod
    def make_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0
        self.seeds_after_bloom = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds = self.seeds_after_bloom


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
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def shade_called(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_dia = trunk_diameter
        self.stats: Tree.Statistics = self.Statistics()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_dia}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}", end="")
        print(f"cm long and {self.trunk_dia}cm wide.")
        self.stats.shade_called()


def display_stats(plant: Plant) -> None:
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? -> ", end="")
    print(Plant.is_older_than_year(30))
    print("Is 400 days more than a year? -> ", end="")
    print(Plant.is_older_than_year(400))

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    display_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.make_anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)


if __name__ == "__main__":
    main()
