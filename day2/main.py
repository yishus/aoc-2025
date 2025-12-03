from pathlib import Path


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def check_all_nines(number):
    """
    Checks if every digit in a given number is 9.

    Args:
      number: An integer or a string representing a number.

    Returns:
      True if all digits are 9, False otherwise.
    """
    num_str = str(number)  # Convert the number to a string
    for digit in num_str:
        if digit != "9":
            return False  # If any digit is not '9', return False
    return True  # If all digits are '9', return True


def solve_part_one(data):
    res = 0
    ranges = data[0].split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        current = start
        while current <= end:
            num_digits = len(str(current))
            if num_digits % 2 == 1:
                current = 10**num_digits
                continue

            first_half = str(current)[: num_digits // 2]
            first_half_int = int(first_half)
            goal = int(first_half + first_half)
            if goal >= start and goal <= end:
                res += goal

            if check_all_nines(first_half_int):
                current = goal + 1
            else:
                current = int(str(first_half_int + 1) + str(first_half_int + 1))

    return res


def solve_part_two(data):
    res = 0
    ranges = data[0].split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        current = start
        while current <= end:
            current_len = len(str(current))
            first_digit_str = str(current)[0]

            for i in range(1, (current_len // 2 + 1)):
                if current_len % i != 0:
                    continue
                repeated_digit_str = str(current)[:i]
                goal = int(repeated_digit_str * (current_len // i))
                while repeated_digit_str[0] == first_digit_str and goal <= end:
                    if i == 1 or not has_repeated_pattern(repeated_digit_str):
                        if goal >= start:
                            res += goal

                    repeated_digit_str = str(int(repeated_digit_str) + 1)
                    goal = int(repeated_digit_str * (current_len // i))

            if first_digit_str == "9":
                current = 10**current_len
            else:
                next_digit = int(first_digit_str) + 1
                current = next_digit * (10 ** (current_len - 1))

    return res


def has_repeated_pattern(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        if length % i == 0:
            pattern = s[:i]
            if pattern * (length // i) == s:
                return True
    return False


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
