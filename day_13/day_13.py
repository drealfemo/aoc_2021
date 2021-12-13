import os
import sys


def fold_on_row(init_grid, y_fold):
    upper_half = init_grid[:y_fold]
    lower_half = init_grid[y_fold+1:][::-1]
    diff = len(upper_half) - len(lower_half)
    for y in range(len(lower_half)):
        sum_row = [n + o for n, o in zip(upper_half[y+diff], lower_half[y])]
        upper_half[y+diff] = [1 if x >= 1 else 0 for x in sum_row]
    return upper_half


def fold_on_col(init_grid, x_fold):
    for x in range(1, x_fold+1):
        upper_col = [a[x_fold+x] for a in init_grid]
        lower_col = [b[x_fold-x] for b in init_grid]
        sum_row = [n + o for n, o in zip(upper_col, lower_col)]
        new_col = [1 if x >= 1 else 0 for x in sum_row]
        for i in range(len(init_grid)):
            init_grid[i][x_fold-x] = new_col[i]
    final_grid = [x[:x_fold] for x in init_grid]
    return final_grid


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()
    space_index = input_list.index("")
    pos = [list(map(int, x.split(",")[::-1])) for x in input_list[:space_index]]
    folds = input_list[space_index+1:]
    folds = [a.split("=") for a in folds]
    folds = [(b[0][-1], b[1][:]) for b in folds]
    lim_row = max(p[0] for p in pos) + 1
    lim_col = max(p[1] for p in pos) + 1

    grid = [[0] * lim_col for _ in range(lim_row)]

    for p in pos:
        grid[p[0]][p[1]] = 1

    for i, fold in enumerate(folds):
        if fold[0] == "y":
            grid = fold_on_row(grid, int(fold[1]))
        else:
            grid = fold_on_col(grid, int(fold[1]))
        if i == 0:
            print(sum([sum(x) for x in grid]))
    for row in grid:
        print(*["#" if x == 1 else "." for x in row])
