from pathlib import Path


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_one(data):
    fresh = 0
    ranges, ingredients = split_input(data)
    merged = merge_ranges(ranges)
    for ingredient in map(int, ingredients):
        range_index = find_largest_valid_range(merged, ingredient)
        current_range = merged[range_index]
        if ingredient >= current_range[0] and ingredient <= current_range[1]:
            fresh += 1
    return fresh


def solve_part_two(data):
    total = 0
    ranges, _ = split_input(data)
    merged = merge_ranges(ranges)
    for m in merged:
        total += m[1] - m[0] + 1

    return total


def split_input(data):
    ranges = []
    ingredients = []
    for index, row in enumerate(data):
        if row != "":
            ranges.append(row)
        else:
            ingredients = data[index + 1 :]
            break

    return ranges, ingredients


def merge_ranges(ranges):
    merged = []
    range_arrays = [list(map(int, r.split("-"))) for r in ranges]
    range_arrays.sort(key=lambda x: x[0])
    for r in range_arrays:
        last = merged[-1] if merged else None
        if last is None or r[0] > last[1]:
            merged.append([r[0], r[1]])
        else:
            merged[-1][1] = max(merged[-1][1], r[1])
    return merged


def find_largest_valid_range(merged, ingredient):
    left = 0
    right = len(merged) - 1

    while left <= right:
        mid = (left + right) // 2
        if merged[mid][0] == ingredient:
            return mid
        elif merged[mid][0] < ingredient:
            left = mid + 1
        else:
            right = mid - 1

    return right


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
