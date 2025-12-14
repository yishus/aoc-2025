from pathlib import Path
import re
from collections import deque


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_one(data):
    res = 0
    indicator_lights, buttons = parse_input(data)
    for i in range(len(indicator_lights)):
        res += bfs(indicator_lights[i], buttons[i])

    return res


def solve_part_two(data):
    pass


def bfs(goal, buttons):
    m = len(buttons)
    queue = deque([([idx], 0) for idx in range(m)])
    while queue:
        buttons_to_toggle, current_value = queue.popleft()
        current_button_idx = buttons_to_toggle[-1]
        result_value = current_value ^ buttons[current_button_idx]
        if result_value == goal:
            return len(buttons_to_toggle)
        for idx in range(current_button_idx + 1, m):
            queue.append((buttons_to_toggle + [idx], result_value))

    return 0


def parse_input(data):
    pattern = r"(\[.*?\])\s(.*)\s(\{.*?\})"
    indicator_lights = []
    buttons = []
    for row in data:
        match = re.search(pattern, row)
        if match:
            part1 = match.group(1)
            part2 = match.group(2)

            size = len(part1) - 2
            indicator_lights.append(extract_indicator_lights(part1))
            buttons.append(extract_button_toggles(part2, size))
        else:
            print("Pattern not found in the string.")

    return (indicator_lights, buttons)


def extract_indicator_lights(s):
    values = list(s[1:-1])
    bit_str = "".join(["1" if v == "#" else "0" for v in values])
    return int(bit_str, 2)


def extract_button_toggles(s, size):
    values = [
        [int(e.strip()) for e in t_str.strip("()").split(",")]
        for t_str in re.findall(r"\(.*?\)", s)
    ]
    res = []
    for v in values:
        bit_str = ["0"] * size
        for i in v:
            bit_str[i] = "1"
        res.append(int("".join(bit_str), 2))
    return res


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
