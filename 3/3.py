from math import pi, sqrt, hypot, atan2, acos, asin
from typing import List, Set, Tuple


class Point:
    def __init__(self, x: float=0.0, y: float=0.0):
        self.x: float = x
        self.y: float = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, k: float):
        return Point(self.x * k, self.y * k)

    def __truediv__(self, k: float):
        return Point(self.x / k, self.y / k)
    
    def __repr__(self):
        return "Point({:.2f}, {:.2f})".format(self.x, self.y)


class Vector:
    def __init__(self, start: Point=Point(), end: Point=Point()):
        self.start: Point = start
        self.end: Point = end
        self.vector: Point = end - start
    
    def __add__(self, other):
        return Vector(self.start + other.start, self.end + other.end)

    def __iadd__(self, other):
        self.start += other.start
        self.end += other.end
        self.vector = self.end - self.start
        return self
    
    def __sub__(self, other):
        return Vector(self.start - other.start, self.end - other.end)

    def __isub__(self, other):
        self.start -= other.start
        self.end -= other.end
        return self
    
    def length(self) -> float:
        return hypot(self.vector.x, self.vector.y)
    
    def __truediv__(self, k: float):
        return Vector(self.start / k, self.end / k)
    
    def __mul__(self, other):
        # dot product
        return self.vector.x * other.vector.x + self.vector.y * other.vector.y

    def __matmul__(self, other):
        # cross product
        return self.vector.x * other.vector.y - self.vector.y * other.vector.x

    def __xor__(self, k: float):
        # scalar product
        return Vector(self.start * k, self.end * k)

    def __repr__(self):
        return "Vector({:.2f}, {:.2f})".format(self.vector.x, self.vector.y)


def clockwiseangle_and_distance(point: Point, origin=Point(0, 0), refvec=Vector(end=Point(0, 1))):
    radius_vector = Vector(origin, point)
    length: float = radius_vector.length()
    if length == 0:
        return -pi, 0
    normalized = radius_vector / length
    dotprod = normalized * refvec
    diffprod = normalized @ refvec
    angle = atan2(diffprod, dotprod)
    if angle < 0:
        return 2 * pi + angle, length
    return angle, length


a, b = map(float, input().split())
h = float(input())
m, n, o, p = map(float, input().split())

O = Point(a, b)
A = Point(m, n)
B = Point(m, p)
C = Point(o, p)
D = Point(o, n)
PROB = 0
if Vector(O, A).length() <= h and Vector(O, B).length() <= h and\
    Vector(O, C).length() <= h and Vector(O, D).length() <= h:
    # rectangle inside circle, no intersection
    rect: List[Point] = [A, B, C, D]
    rect.sort(key=lambda p: clockwiseangle_and_distance(p, origin=Point(a, b))[1])
    max_angle = -float('inf')
    for i in range(len(rect)):
        for j in range(i + 1, len(rect)):
            vec_a = Vector(O, rect[i])
            vec_b = Vector(O, rect[j])
            
            vec_a_len = vec_a.length()
            vec_b_len = vec_b.length()
            
            angle_a_b_cos = acos((vec_a * vec_b) / (vec_a_len * vec_b_len))
            max_angle = max(max_angle, angle_a_b_cos)
    
    PROB = max_angle / (2 * pi)
else:
    # intersection exists
    intersects_set: Set[Tuple[Point, int]] = set()
    # bottom line intersect
    bottom_c1 = a * a - h * h + n * n - 2 * b * n + b * b
    bottom_d = 4 * a * a - 4 * bottom_c1
    if bottom_d >= 0:
        bottom_x1 = (2 * a - sqrt(bottom_d)) / 2
        if m <= bottom_x1 <= o:
            intersects_set.add((Point(bottom_x1, n), 0))
        bottom_x2 = (2 * a + sqrt(bottom_d)) / 2
        if m <= bottom_x2 <= o:
            intersects_set.add((Point(bottom_x2, n), 0))
    # top line intersect
    top_c1 = a * a - h * h + p * p - 2 * b * p + b * b
    top_d = 4 * a * a - 4 * top_c1
    if top_d >= 0:
        top_x1 = (2 * a - sqrt(top_d)) / 2
        if m <= top_x1 <= o:
            intersects_set.add((Point(top_x1, p), 0))
        top_x2 = (2 * a + sqrt(top_d)) / 2
        if m <= top_x2 <= o:
            intersects_set.add((Point(top_x2, p), 0))
    # left line intersect
    left_c1 = h * h - (m - a) ** 2
    if left_c1 >= 0:
        left_y1 = sqrt(left_c1) + b
        if n <= left_y1 <= p:
            intersects_set.add((Point(m, left_y1), 0))
        left_y2 = -sqrt(left_c1) + b
        if n <= left_y2 <= p:
            intersects_set.add((Point(m, left_y2), 0))
    # right line intersect
    right_c1 = h * h - (o - a) ** 2
    if right_c1 >= 0:
        right_y1 = sqrt(right_c1) + b
        if n <= right_y1 <= p:
            intersects_set.add((Point(o, right_y1), 0))
        right_y2 = -sqrt(right_c1) + b
        if n <= right_y2 <= p:
            intersects_set.add((Point(o, right_y2), 0))

    for pts in A, B, C, D:
        if Vector(O, pts).length() <= h:
            intersects_set.add((pts, 1))
    intersects: List[Tuple[Point, int]] = sorted(intersects_set, key=lambda p: clockwiseangle_and_distance(p[0], origin=Point(a, b)))
    intersects.append(intersects[0]) # at least one element in `intersects` as circle center is outside the rectangle

    l1 = 0
    l2 = 2 * pi
    for i in range(len(intersects) - 1):
        vec_a: Vector = Vector(O, intersects[i][0])
        vec_b: Vector = Vector(O, intersects[i + 1][0])
        vec_m: Vector = vec_a + vec_b
        
        vec_a_len = vec_a.length()
        vec_b_len = vec_b.length()
        vec_m_len = vec_m.length()
        
        vec_m = vec_m / vec_m_len
        vec_m = vec_m ^ h
        vec_m = Vector(end=O) + vec_m

        angle_a_b_sin = asin((vec_b @ vec_a) / (vec_a_len * vec_b_len))
        angle_a_b_cos = acos((vec_a * vec_b) / (vec_a_len * vec_b_len))

        if angle_a_b_sin < 0:
            r_vec = Vector(end=O) - vec_m
            vec_m = vec_m + (r_vec ^ 2)
        
        if m <= vec_m.vector.x <= o and n <= vec_m.vector.y <= p or ((intersects[i][1] == 1 or intersects[i + 1][1] == 1) and angle_a_b_sin >= 0):
            if angle_a_b_sin < 0:
                l1 += 2 * pi - angle_a_b_cos
            else:
                l1 += angle_a_b_cos
    
    PROB = l1 / l2

print("{:.3f}".format(PROB))
