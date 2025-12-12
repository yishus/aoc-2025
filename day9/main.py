from pathlib import Path
import shapely


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [list(map(int, line.strip().split(","))) for line in f]


def solve_part_one(data):
    max_area = 0
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            p1 = data[i]
            p2 = data[j]
            area = area_of_rect_from_coords(p1, p2)
            if area > max_area:
                max_area = area

    return max_area


def solve_part_two(data):
    areas = []
    polygon = shapely.Polygon(data)
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            p1 = data[i]
            p2 = data[j]
            areas.append((area_of_rect_from_coords(p1, p2), p1, p2))

    areas.sort(reverse=True)

    for area, p1, p2 in areas:
        rect_from_coords = shapely.Polygon((p1, (p1[0], p2[1]), p2, (p2[0], p1[1])))
        if polygon.contains(rect_from_coords):
            return area

    #         print(p1, p2)
    #
    #         lines = [
    #             shapely.LineString([p1, (p1[0], p2[1])]),
    #             shapely.LineString([(p1[0], p2[1]), p2]),
    #             shapely.LineString([p2, (p2[0], p1[1])]),
    #             shapely.LineString([(p2[0], p1[1]), p1]),
    #         ]
    #
    #         for line in lines:
    #             print(p1, p2, line, polygon.intersection(line))
    #
    #         # if not any(polygon.intersects(line) for line in lines):
    #         #     area = area_of_rect_from_coords(p1, p2)
    #         #     if area > max_area:
    #         #         max_area = area
    #
    # return max_area
    #


def area_of_rect_from_coords(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (abs(y2 - y1) + 1) * (abs(x2 - x1) + 1)


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
