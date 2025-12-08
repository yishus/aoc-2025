from pathlib import Path
from collections import defaultdict


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_one(data):
    res = 0
    targets = {data[0].find("S")}
    for row in data[1:]:
        next_targets = set()
        for t in targets:
            if row[t] == ".":
                next_targets.add(t)
            else:
                res += 1
                next_targets.add(t - 1)
                next_targets.add(t + 1)
        targets = next_targets

    return res


def solve_part_two(data):
    res = 1
    starting_pos = data[0].find("S")
    targets = {starting_pos: 1}
    for row in data[1:]:
        next_targets = defaultdict(int)
        for t, count in targets.items():
            if row[t] == ".":
                next_targets[t] += count
            else:
                res += count
                next_targets[t - 1] += count
                next_targets[t + 1] += count
        targets = next_targets

    return res


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
