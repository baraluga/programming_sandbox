BOMB_STATE_MACHINE = [
    {"white": 1, "red": 2},
    {"white": 2, "orange": 3},
    {"black": 3, "red": 0},
    {"green": 4, "orange": 5, "black": 3},
    {"orange": 6},
    {"green": 6},
    None
]


def defuse(wire_combination: list):
    is_defusable = True
    current_state = BOMB_STATE_MACHINE[0]  # start at the initial state!
    for wire_to_cut in wire_combination:
        print(f"About to cut {wire_to_cut} from {current_state.keys()}")
        if wire_to_cut not in current_state.keys():
            is_defusable = False
            break
        current_state = BOMB_STATE_MACHINE[current_state[wire_to_cut]]
    return is_defusable


if __name__ == "__main__":
    DEFUSABLE_INPUT = ["white", "white", "red", "white",
                       "orange", "black", "black", "green", "orange"]
    BOOMABLE_INPUT = ["white", "white", "green", "orange", "green"]
    DEFUSABLE_INPUT_2 = ["white", "white", "red", "red", "red", "white",
                         "white", "black", "green", "orange"]

    print("defused" if defuse(DEFUSABLE_INPUT_2) else "boom")
