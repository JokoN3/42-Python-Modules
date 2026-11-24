import sys


def attempt_read(file_name: str) -> None:
    file = None
    try:
        file = open(file_name, "r")
        content: str = file.read()
        print("---\n\n")
        print(content)
        print("\n\n---")
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


def main() -> None:
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    attempt_read(sys.argv[1])



if __name__ == "__main__":
    main()
