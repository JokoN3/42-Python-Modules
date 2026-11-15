import sys


def parse_input(args: list[str]) -> dict[str, int]:
    inventory: dict = {}
    for item in args:
        try:
            curr_item: list[str] = item.split(":")
            if len(curr_item) != 2:
                print(f"Error - invalid parameter '{item}'")
                continue
            item_name: str = curr_item[0]
            item_quanitity: int = int(curr_item[1])
            if item_name in inventory:
                print(f"Redundant item '{item_name}' - discarding")
                continue
            inventory[item_name] = item_quanitity
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
        except Exception:
            print(f"Error - invalid parameter '{item}'")
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict = parse_input(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_quantity: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")
    
    items_list = list(inventory.keys())
    most_abundant: str = items_list[0]
    least_abundant: str = items_list[0]
    first_run: bool = True
    if total_quantity > 0:
        for item in inventory.keys():
            qty: int = inventory[item]
            if qty > inventory[most_abundant]:
                most_abundant = item
            if qty < inventory[least_abundant]:
                least_abundant = item
            item_percent: float = (qty / total_quantity) * 100

            print(f" Item {item} represents {item_percent:.1f}%")
    else:
        print("Inventory empty")

    print(f"Item most abundant: {most_abundant} with "
          f"quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} "
          f"with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
