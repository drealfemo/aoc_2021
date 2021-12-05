import os
import sys
from collections import Counter


def all_points(p1, p2, allow_diagonal=False):
    p1 = list(map(int, p1))
    p2 = list(map(int, p2))
    if p1[0] == p2[0] or p1[1] == p2[1]:
        xs = range(min(p1[0], p2[0]), max(p1[0], p2[0])) or [p1[0]]
        ys = range(min(p1[1], p2[1]), max(p1[1], p2[1])) or [p1[1]]
        ps = [(x, y) for x in xs for y in ys]
        if len(xs) == 1:
            return ps + [(xs[0], max(p1[1], p2[1]))]
        elif len(ys) == 1:
            return ps + [(max(p1[0], p2[0]), ys[0])]
    elif allow_diagonal:
        rev = False
        if abs(p1[0] - p2[0]) == abs(p1[1] - p2[1]):
            xs = []
            if p1[0] > p2[0]:
                rev = True
            for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
                xs.append(x)
            if rev:
                xs = xs[::-1]
            rev = False

            ys = []
            if p1[1] > p2[1]:
                rev = True
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                ys.append(y)
            if rev:
                ys = ys[::-1]

            ps = list(zip(xs, ys))
            return ps
    return []


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = [x.split(" -> ") for x in f.read().splitlines()]
        input_list = [[y.split(",") for y in x] for x in input_list]

    # part one
    line_points = []
    for points in input_list:
        line_points.extend(all_points(points[0], points[1]))
    line_points = Counter(line_points)
    final_points_one = {k: v for k, v in line_points.items() if v >= 2}
    print(len(final_points_one))

    # part two
    line_points = []
    for points in input_list:
        line_points.extend(all_points(points[0], points[1], allow_diagonal=True))
    line_points = Counter(line_points)
    final_points_two = {k: v for k, v in line_points.items() if v >= 2}
    print(len(final_points_two))
