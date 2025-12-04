from pathlib import Path
import heapq


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_one(data):
    res = 0
    for row in data:
        res += largest_joltage(2, row)
    return res


def solve_part_two(data):
    res = 0
    for row in data:
        res += largest_joltage(12, row)
    return res


def largest_joltage(size, batteries):
    res = 0
    start_index = 0
    for s in range(size - 1, -1, -1):
        end_index = len(batteries) - s
        digit_heap = [
            (digit, -1 * (start_index + index))
            for index, digit in enumerate(
                [int(d) for d in list(batteries[start_index:end_index])]
            )
        ]
        heapq.heapify_max(digit_heap)
        largest_earliest = digit_heap[0]
        start_index = abs(largest_earliest[1]) + 1
        res += largest_earliest[0] * 10**s

    return res


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
