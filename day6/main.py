from pathlib import Path


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.replace("\n", "") for line in f]


def solve_part_one(data):
    res = 0
    rows = []
    for row in data:
        parts = row.split()
        rows.append(parts)

    for j in range(len(rows[0])):
        problem = []
        for i in range(len(rows)):
            problem.append(rows[i][j])

        result = 0
        operation = problem[-1]
        if operation == "+":
            for number in problem[:-1]:
                result += int(number)
        elif operation == "*":
            result = 1
            for number in problem[:-1]:
                result *= int(number)

        res += result

    return res


def solve_part_two(data):
    res = 0
    operators_row = data[-1]
    operators = operators_row.split()
    m = len(data) - 1
    question_count = 0
    numbers = []
    column = []
    for j in range(len(data[0])):
        for i in range(m):
            column.append(data[i][j])

        if all(x == " " for x in column):
            op = operators[question_count]
            result = 0 if op == "+" else 1
            for number in numbers:
                if op == "+":
                    result += number
                elif op == "*":
                    result *= number

            res += result
            question_count += 1
            numbers = []
            continue

        filtered_column = filter(lambda x: x != " ", column)
        number = 0
        for idx, n in enumerate(reversed(list(filtered_column))):
            number += int(n) * 10**idx
        numbers.append(number)
        column = []

    op = operators[question_count]
    result = 0 if op == "+" else 1
    for number in numbers:
        if op == "+":
            result += number
        elif op == "*":
            result *= number

    res += result

    return res


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
