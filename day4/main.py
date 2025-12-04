from pathlib import Path
import copy


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [list(line.strip()) for line in f]


def solve_part_one(data):
    paper = copy.deepcopy(data)
    return len(removable_paper(paper))


def solve_part_two(data):
    res = 0
    paper = copy.deepcopy(data)
    while True:
        removable_pos = removable_paper(paper)
        if len(removable_pos) == 0:
            break
        res += len(removable_pos)
        for i, j in removable_pos:
            paper[i][j] = "."
        for i in range(len(paper)):
            for j in range(len(paper[0])):
                if paper[i][j] != ".":
                    paper[i][j] = "@"

    return res


def removable_paper(data):
    res = []
    m = len(data)
    n = len(data[0])
    for i in range(m):
        for j in range(n):
            if data[i][j] == ".":
                continue
            top, middle, bottom = 0, 1, 0
            if i > 0:
                prev_row = data[i - 1][j]
                if prev_row == ".":
                    if j > 0:
                        top += 1 if data[i - 1][j - 1] != "." else 0
                        middle += 1 if data[i][j - 1] != "." else 0
                    if j < n - 1:
                        top += 1 if data[i - 1][j + 1] != "." else 0
                        middle += 1 if data[i][j + 1] != "." else 0
                else:
                    top = data[i - 1][j][0]
                    middle = data[i - 1][j][1]
            else:
                if j > 0:
                    middle += 1 if data[i][j - 1] != "." else 0
                if j < n - 1:
                    middle += 1 if data[i][j + 1] != "." else 0
            if i < m - 1:
                bottom += 1 if data[i + 1][j] == "@" else 0
                if j > 0:
                    bottom += 1 if data[i + 1][j - 1] == "@" else 0
                if j < n - 1:
                    bottom += 1 if data[i + 1][j + 1] == "@" else 0
            data[i][j] = (middle, bottom)
            if top + middle + bottom <= 4:
                res.append((i, j))
    return res


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
