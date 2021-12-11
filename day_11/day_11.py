import os
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = [list(map(int, list(x))) for x in f.read().splitlines()]

    row_size = len(input_list)
    col_size = len(input_list[0])
    step = 0
    num_flashes = 0
    step_all_flashed = None
    while not step_all_flashed:
        input_list = [[y + 1 for y in x] for x in input_list]
        flashed_arr = [(i, j) for i, row in enumerate(input_list) for j, val in enumerate(row) if val > 9]
        all_flashed = []
        all_flashed.extend(flashed_arr)

        def update_energy_levels_for_flashed(flashed):
            new_flashed = []
            for pos in flashed:
                i, j = pos[0], pos[1]
                input_list[i][j] = 0

                # up
                if i-1 >= 0:
                    if (p := (i-1, j)) not in all_flashed:
                        input_list[i - 1][j] += 1
                        if input_list[i - 1][j] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
                # down
                if i+1 < row_size:
                    if (p := (i+1, j)) not in all_flashed:
                        input_list[i + 1][j] += 1
                        if input_list[i + 1][j] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
                # left
                if j-1 >= 0:
                    if (p := (i, j-1)) not in all_flashed:
                        input_list[i][j - 1] += 1
                        if input_list[i][j - 1] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
                # right
                if j+1 < col_size:
                    if (p := (i, j+1)) not in all_flashed:
                        input_list[i][j + 1] += 1
                        if input_list[i][j + 1] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
                # up-left
                if i-1 >= 0 and j-1 >= 0:
                    if (p := (i-1, j-1)) not in all_flashed:
                        input_list[i - 1][j - 1] += 1
                        if input_list[i - 1][j - 1] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
                # up-right
                if i-1 >= 0 and j+1 < col_size:
                    if (p := (i-1, j+1)) not in all_flashed:
                        input_list[i - 1][j + 1] += 1
                        if input_list[i - 1][j + 1] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
                # down-left
                if i+1 < row_size and j-1 >= 0:
                    if (p := (i+1, j-1)) not in all_flashed:
                        input_list[i + 1][j - 1] += 1
                        if input_list[i + 1][j - 1] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
                # down-right
                if i+1 < row_size and j+1 < col_size:
                    if (p := (i+1, j+1)) not in all_flashed:
                        input_list[i + 1][j + 1] += 1
                        if input_list[i + 1][j + 1] > 9:
                            new_flashed.append(p)
                            all_flashed.append(p)
            else:
                if new_flashed:
                    update_energy_levels_for_flashed(new_flashed)
        update_energy_levels_for_flashed(flashed_arr)
        if step < 100:
            num_flashes += len(all_flashed)
        if len(all_flashed) == row_size * col_size:
            step_all_flashed = step + 1
        step += 1

    print(num_flashes)  # part 1
    print(step_all_flashed)  # part 2
