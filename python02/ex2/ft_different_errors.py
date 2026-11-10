def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file", "r",)
    elif operation_number == 3:
        5 + 'abc'
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for op in range(5):
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nTesting multiple errors in one try block...")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError,
            FileNotFoundError, TypeError) as e:
        print(f"Caught an error: {e}")
    print("\nAll error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
