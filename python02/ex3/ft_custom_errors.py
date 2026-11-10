class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def plant_status() -> None:
    raise PlantError("The tomato plant is wilting!")


def tank_status() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant_status()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        tank_status()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        plant_status()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        tank_status()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
