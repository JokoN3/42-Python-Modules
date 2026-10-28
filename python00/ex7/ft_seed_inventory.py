def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize() + " seeds"
    if unit not in ("packets", "grams", "area"):
        print("Unknown unit type")
        return
    if unit == "packets":
        print(f"{seed_type}: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type}: {quantity} grams total")
    else:
        print(f"{seed_type}: covers {quantity} square meters")
