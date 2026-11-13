import math


def get_player_pos() -> tuple:
    while True:
        full_str: str = input("Enter new coordinates as "
                              "floats in format 'x,y,z': ")
        str_list: list[str] = full_str.split(',')
        float_list: list[float] = []
        if len(str_list) != 3:
            print("Invalid syntax")
            continue
        for s in str_list:
            s = s.strip()
            try:
                float_list.append(float(s))
            except ValueError as e:
                print(f"Error on parameter '{s}': {e}")
                break

        if len(float_list) == 3:
            coordinates = tuple(float_list)
            break
        else:
            continue

    return coordinates


def calculate_distance_to_center(coord: tuple) -> None:
    x1, y1, z1 = coord
    distance: float = math.sqrt(x1**2 + y1**2 + z1**2)
    distance = round(distance, 4)
    print(f"Distance to center: {distance}")


def calc_dist_between_positions(coord1: tuple, coord2: tuple) -> None:
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    distance: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    distance = round(distance, 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coord1: tuple = get_player_pos()
    x, y, z = coord1
    print(f"Got a first tuple: {coord1}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    calculate_distance_to_center(coord1)

    print("\nGet a second set of coordinates")
    coord2: tuple = get_player_pos()
    calc_dist_between_positions(coord1, coord2)


if __name__ == "__main__":
    main()
