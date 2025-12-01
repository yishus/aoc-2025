from pathlib import Path


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_one(data):
    res = 0
    safeValue = 50
    for d in data:
        direction = d[0]
        val = d[1:]
        match direction:
            case "L":
                safeValue -= int(val)
            case "R":
                safeValue += int(val)

        if safeValue > 99 or safeValue < 0:
            safeValue = safeValue % 100

        if safeValue == 0:
            res += 1

    return res


def solve_part_two(data):
    res = 0
    safeValue = 50
    for d in data:
        started_at_zero = safeValue == 0
        direction = d[0]
        val = d[1:]
        match direction:
            case "L":
                safeValue -= int(val)
            case "R":
                safeValue += int(val)

        if safeValue == 0:
            res += 1

        if safeValue > 99 or safeValue < 0:
            if safeValue < 0 and not started_at_zero:
                res += 1
            res += abs(safeValue) // 100
            safeValue = safeValue % 100

    return res


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
