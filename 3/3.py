from math import pi, sqrt, hypot, atan2, degrees, acos, asin


def clockwiseangle_and_distance(point, origin=[0, 0], refvec=[0, 1]):
    radius_vector = [point[0] - origin[0], point[1] - origin[1]]
    length = hypot(radius_vector[0], radius_vector[1])
    if length == 0:
        return -pi, 0
    normalized = [radius_vector[0] / length, radius_vector[1] / length]
    dotprod = normalized[0] * refvec[0] + normalized[1] * refvec[1]
    diffprod = refvec[1] * normalized[0] - refvec[0] * normalized[1]
    angle = atan2(diffprod, dotprod)
    if angle < 0:
        return 2 * pi + angle, length
    return angle, length


a, b = map(float, input().split())
h = float(input())
m, n, o, p = map(float, input().split())
if m > o:
    m, o = o, m
    n, p = p, n

DIST_A = hypot(m - a, n - b)
DIST_B = hypot(m - a, p - b)
DIST_C = hypot(o - a, p - b)
DIST_D = hypot(o - a, n - b)
PROB = 0
if DIST_A <= h and DIST_B <= h and DIST_C <= h and DIST_D <= h:
    # rectangle inside circle, no intersection
    rect = [[m, n], [m, p], [o, p], [o, n]]
    rect.sort(key=lambda p: clockwiseangle_and_distance(p, origin=[a, b])[1])
    rect = rect[:2]
    vec_a = [rect[0][0] - a, rect[0][1] - b]
    vec_b = [rect[1][0] - a, rect[1][1] - b]
    vec_a_len = hypot(vec_a[0], vec_a[1])
    vec_b_len = hypot(vec_b[0], vec_b[1])
    
    angle_a_b_sin = acos((vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1]) / (vec_a_len * vec_b_len))
    
    PROB = angle_a_b_sin * h / (2 * pi * h)
elif a - m > h and o - a > h and b - n > h and p - b > h:
    # circle inside rectangle, no intersection
    PROB = 1
else:
    # intersection
    intersects = set()
    # bottom line intersect
    bottom_c1 = a * a - h * h + n * n - 2 * b * n + b * b
    D = 4 * a * a - 4 * bottom_c1
    if D >= 0:
        bottom_x1 = (2 * a - sqrt(D)) / 2
        if m <= bottom_x1 <= o:
            intersects.add((bottom_x1, n))
        bottom_x2 = (2 * a + sqrt(D)) / 2
        if m <= bottom_x2 <= o:
            intersects.add((bottom_x2, n))
    # top line intersect
    top_c1 = a * a - h * h + p * p - 2 * b * p + b * b
    D = 4 * a * a - 4 * top_c1
    if D >= 0:
        top_x1 = (2 * a - sqrt(D)) / 2
        if m <= top_x1 <= o:
            intersects.add((top_x1, p))
        top_x2 = (2 * a + sqrt(D)) / 2
        if m <= top_x2 <= o:
            intersects.add((top_x2, p))
    # left line intersect
    left_c1 = h * h - (m - a) ** 2
    if left_c1 >= 0:
        left_y1 = sqrt(left_c1) + b
        if n <= left_y1 <= p:
            intersects.add((m, left_y1))
        left_y2 = -sqrt(left_c1) + b
        if n <= left_y2 <= p:
            intersects.add((m, left_y2))
    # right line intersect
    right_c1 = h * h - (o - a) ** 2
    if right_c1 >= 0:
        right_y1 = sqrt(right_c1) + b
        if n <= right_y1 <= p:
            intersects.add((o, right_y1))
        right_y2 = -sqrt(right_c1) + b
        if n <= right_y2 <= p:
            intersects.add((o, right_y2))

    intersects = sorted(intersects, key=lambda p: clockwiseangle_and_distance(p, origin=[a, b]))
    intersects.append(intersects[0])

    l1 = 0
    l2 = 2 * pi * h
    for i in range(len(intersects) - 1):
        vec_a = [intersects[i][0] - a, intersects[i][1] - b]
        vec_b = [intersects[i + 1][0] - a, intersects[i + 1][1] - b]
        vec_m = [vec_a[0] + vec_b[0], vec_a[1] + vec_b[1]]
        
        vec_a_len = hypot(vec_a[0], vec_a[1])
        vec_b_len = hypot(vec_b[0], vec_b[1])
        m_len = hypot(vec_m[0], vec_m[1])
        
        vec_m = [vec_m[0] / m_len, vec_m[1] / m_len]
        vec_m = [vec_m[0] * h, vec_m[1] * h]
        vec_m = [a + vec_m[0], b + vec_m[1]]

        angle_a_b_sin = asin((vec_b[0] * vec_a[1] - vec_b[1] * vec_a[0]) / (vec_a_len * vec_b_len))
        angle_a_b_cos = acos((vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1]) / (vec_a_len * vec_b_len))
        if angle_a_b_sin < 0:
            r_vec = [a - vec_m[0], b - vec_m[1]]
            vec_m = [vec_m[0] + 2 * r_vec[0], vec_m[1] + 2 * r_vec[1]]
        
        if m <= vec_m[0] <= o and n <= vec_m[1] <= p:
            if angle_a_b_sin < 0:
                l1 += l2 - angle_a_b_cos * h
            else:
                l1 += angle_a_b_cos * h
    
    PROB = l1 / l2

print("{:.3f}".format(PROB))
