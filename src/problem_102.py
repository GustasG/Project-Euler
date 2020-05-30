class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

origin = Point(0, 0)

def read_file(file_name: str) -> list:
    triangles = []

    with open(file_name, 'r') as f:
        for line in f:
            coordinates = list(map(int, line.split(',')))

            a = Point(coordinates[0], coordinates[1])
            b = Point(coordinates[2], coordinates[3])
            c = Point(coordinates[4], coordinates[5])

            triangles.append(Triangle(a, b, c))

    return triangles

def sign(p1: Point, p2: Point, p3: Point) -> int:
    return (p1.x - p3.x)*(p2.y - p3.y) - (p2.x - p3.x)*(p1.y - p3.y)

def contains_origin(triangle: Triangle) -> bool:
    d1 = sign(origin, triangle.a, triangle.b)
    d2 = sign(origin, triangle.b, triangle.c)
    d3 = sign(origin, triangle.c, triangle.a)

    has_negative = d1<0 or d2<0 or d3<0
    has_positive = d1>0 or d2>0 or d3>0

    return not(has_negative and has_positive)

def main():
    triangles = read_file('problem_102_triangles.txt')
    total = sum(contains_origin(t) for t in triangles)
    print(total)

if __name__ == "__main__":
    main()