def input_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature err: {e}")
        return None
    else:
        print(f"Temperature is now {temp}°C")
        return temp


def main() -> None:
    print("=== Garden Temperature ===\n")
    input_str = "25"
    print("Input data is '25'")
    input_temperature(input_str)

    input_str = "abc"
    print("\nInput data is 'abc'")
    input_temperature(input_str)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
