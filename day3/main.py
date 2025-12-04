from pathlib import Path
import heapq


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_one(data):
    res = 0
    for row in data:
        first_digit_heap = [
            (digit, -1 * index)
            for index, digit in enumerate([int(d) for d in list(row[:-1])])
        ]
        heapq.heapify_max(first_digit_heap)
        largest_earliest = first_digit_heap[0]
        second_digit_heap = [int(d) for d in list(row[abs(largest_earliest[1]) + 1 :])]
        heapq.heapify_max(second_digit_heap)
        res += largest_earliest[0] * 10 + second_digit_heap[0]

    return res


def solve_part_two(data):
    pass


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
