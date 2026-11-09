def input_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature err: {e}")
        return None
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        return temp


def test_temperature(input_str: str) -> None:
    print(f"Input data is '{input_str}'")
    try:
        temp = input_temperature(input_str)
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")

    test_temperature("abc")

    test_temperature("100")

    test_temperature("-50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
