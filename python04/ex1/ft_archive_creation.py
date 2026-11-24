import sys
from typing import IO, Optional


def transform_data(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed: list[str] = []
    for line in lines:
        transformed.append(f"{line}#\n")
    return "".join(transformed)


def get_name(content: str) -> None:
    new_file_name: str = input("Enter new file name (or empty):")
    new_file: Optional[IO[str]] = None
    if new_file_name == "":
        print("Not saving data.")
        return
    else:
        try:
            new_file = open(new_file_name, "w")
            new_file.write(content)
        except Exception as e:
            print(f"{e}")
        finally:
            if new_file is not None:
                new_file.close()


def archive_creation(file_name: str) -> None:
    file = None
    try:
        file = open(file_name, "r")
        content: str = file.read()
        print("---\n")
        print(content)
        print("\n---")
    except FileNotFoundError as e:
        print(f"Error opening file '{file_name}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_name}': {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")

    print("\nTransform data:")
    transformed = transform_data(content)
    print("---\n")
    print(transformed)
    print("\n---")
    get_name(transformed)


def main() -> None:
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    archive_creation(sys.argv[1])


if __name__ == "__main__":
    main()
