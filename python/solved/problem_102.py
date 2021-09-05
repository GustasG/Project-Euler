from dataclasses import dataclass
from typing import List

from shared.paths import RESOURCE_DIR


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Triangle:
    a: Point
    b: Point
    c: Point


ORIGIN = Point(0, 0)


def read_file(path: str) -> List[Triangle]:
    with open(path, 'r') as f:
        triangles = []
        for line in f:
            coordinates = list(map(int, line.split(',')))
            points = [Point(coordinates[i], coordinates[i + 1]) for i in range(0, len(line.split(',')), 2)]
            triangles.append(Triangle(*points))

        return triangles


def sign(p1: Point, p2: Point, p3: Point) -> int:
    return (p1.x - p3.x)*(p2.y - p3.y) - (p2.x - p3.x)*(p1.y - p3.y)


def contains_origin(triangle: Triangle) -> bool:
    d1 = sign(ORIGIN, triangle.a, triangle.b)
    d2 = sign(ORIGIN, triangle.b, triangle.c)
    d3 = sign(ORIGIN, triangle.c, triangle.a)

    has_negative = d1 < 0 or d2 < 0 or d3 < 0
    has_positive = d1 > 0 or d2 > 0 or d3 > 0

    return not(has_negative and has_positive)


def main():
    triangles = read_file(RESOURCE_DIR / 'problem_102_triangles.txt')
    total = sum(contains_origin(t) for t in triangles)
    print(total)


if __name__ == "__main__":
    main()
