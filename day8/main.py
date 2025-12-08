from pathlib import Path
import math
import heapq
from functools import reduce


def read_input(filename):
    path = Path(__file__).with_name(filename)
    with open(path, "r") as f:
        return [line.strip() for line in f]


def solve_part_one(data):
    points = list(map(lambda line: tuple(map(int, line.split(","))), data))
    distances = find_distances_in_points(points)
    thousand_closest = closest_k_pairs(distances, 1000)

    uf = UnionFind()
    for point in thousand_closest:
        point1 = "".join(str(item) for item in point[1])
        point2 = "".join(str(item) for item in point[2])
        uf.make_set(point1)
        uf.make_set(point2)
        uf.union(point1, point2)
    cluster_sizes = [len(cluster) for cluster in uf.groups().values()]
    cluster_sizes.sort(reverse=True)

    return reduce(lambda x, y: x * y, cluster_sizes[:3])


def solve_part_two(data):
    points = list(map(lambda line: tuple(map(int, line.split(","))), data))
    distances = find_distances_in_points(points)
    distances.sort(key=lambda x: x[0])

    last_two_points = None
    uf = UnionFind()
    for distance in distances:
        point1 = ",".join(str(item) for item in distance[1])
        point2 = ",".join(str(item) for item in distance[2])
        uf.make_set(point1)
        uf.make_set(point2)
        uf.union(point1, point2)
        values = list(uf.groups().values())
        if len(values) == 1 and len(values[0]) == len(points):  # All sets connected
            last_two_points = [distance[1], distance[2]]
            break

    return (
        last_two_points[0][0] * last_two_points[1][0] if last_two_points else 0
    )  # Just a placeholder to avoid errors


def find_distances_in_points(points):
    distances = []
    for index, point in enumerate(points[:-1]):
        for other_point in points[index + 1 :]:
            distances.append((math.dist(point, other_point), point, other_point))
    return distances


def closest_k_pairs(distances, k):
    heap = []
    for distance in distances:
        if len(heap) < k:
            heapq.heappush_max(heap, distance)
        else:
            heapq.heappushpop_max(heap, distance)

    return heap


class UnionFind:
    def __init__(self):
        # parent dictionary maps each element to its parent
        self.parent = {}
        # size dictionary maps each root element to the size of its set
        # (used for union by size optimization)
        self.size = {}

    def make_set(self, element):
        """
        Initializes a new set with the given element.
        If the element already exists, it does nothing.
        """
        if element not in self.parent:
            self.parent[element] = element  # Element is its own parent initially
            self.size[element] = 1  # Size of the set is 1

    def find(self, element):
        """
        Finds the representative (root) of the set containing the element.
        Applies path compression for optimization.
        """
        if element not in self.parent:
            raise ValueError(f"Element '{element}' not found in any set.")

        # Path compression: if element is not its own parent, recursively find
        # the root and set it as the direct parent of the element.
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, element1, element2):
        """
        Unites the sets containing element1 and element2.
        Applies union by size optimization.
        """
        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            # Union by size: attach the smaller tree under the root of the larger tree
            if self.size[root1] < self.size[root2]:
                root1, root2 = root2, root1  # Swap to ensure root1 is the larger tree

            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            return True  # Union occurred
        return False  # Elements were already in the same set

    def groups(self):
        """
        Returns a dictionary mapping each root to the list of its elements.
        """
        result = {}
        for element in self.parent:
            root = self.find(element)
            if root not in result:
                result[root] = []
            result[root].append(element)
        return result


if __name__ == "__main__":
    input_data = read_input("input.txt")

    # Part One
    result_part_one = solve_part_one(input_data)
    print(f"Part One: {result_part_one}")

    # Part Two
    result_part_two = solve_part_two(input_data)
    print(f"Part Two: {result_part_two}")
