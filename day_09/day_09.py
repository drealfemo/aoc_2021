import os
import sys
from functools import reduce


def get_low_points_and_basin_size(points_arr):
    low_points = []
    low_points_pos = []
    row_size = len(points_arr[0])
    col_size = len(points_arr)
    for i, row in enumerate(points_arr):
        for j, point in enumerate(row):
            if i - 1 >= 0:
                if point >= points_arr[i - 1][j]:
                    continue

            if i + 1 < col_size:
                if point >= points_arr[i + 1][j]:
                    continue

            if j - 1 >= 0:
                if point >= points_arr[i][j - 1]:
                    continue

            if j + 1 < row_size:
                if point >= points_arr[i][j + 1]:
                    continue

            low_points.append(point + 1)
            low_points_pos.append((i, j))

    def find_basin(pos, positions=None):
        if positions is None:
            positions = []
        positions.append(pos)
        i, j = pos[0], pos[1]
        point = input_list[i][j]
        max_diff = 9 - point

        if i - 1 >= 0:
            if abs(point - points_arr[i - 1][j]) < max_diff:
                if (p := (i - 1, j)) not in positions:
                    positions = find_basin(p, positions)

        if i + 1 < col_size:
            if abs(point - points_arr[i + 1][j]) < max_diff:
                if (p := (i + 1, j)) not in positions:
                    positions = find_basin(p, positions)

        if j - 1 >= 0:
            if abs(point - points_arr[i][j - 1]) < max_diff:
                if (p := (i, j - 1)) not in positions:
                    positions = find_basin(p, positions)

        if j + 1 < row_size:
            if abs(point - points_arr[i][j + 1]) < max_diff:
                if (p := (i, j + 1)) not in positions:
                    positions = find_basin(p, positions)

        return positions

    basin_sizes = []
    for point_pos in low_points_pos:
        basin_ps = set(find_basin(point_pos, []))
        basin_sizes.append(len(basin_ps))

    basin_sizes.sort()
    top_three_basins = basin_sizes[-3:]
    basins_mult = reduce(lambda x, y: x*y, top_three_basins)

    return sum(low_points), basins_mult


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = [list(map(int, list(x))) for x in f.read().splitlines()]

    res_one, res_two = get_low_points_and_basin_size(input_list)

    print(res_one)
    print(res_two)
