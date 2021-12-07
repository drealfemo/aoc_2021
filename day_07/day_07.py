import os
import sys
import pandas as pd


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = list(map(int, [x.split(",") for x in f.read().splitlines()][0]))
    possible_pos = [x for x in range(min(*input_list), int(max(*input_list)/2))]

    # part one
    fuel_cost = 9999999999999
    a = pd.Series(input_list)
    for v in possible_pos:
        b = a.copy()
        b = abs(b - v)
        if (cost := b.sum()) < fuel_cost:
            fuel_cost = cost
    print(fuel_cost)

    # part two
    fuel_cost = 9999999999999
    a = pd.Series(input_list)
    for v in possible_pos:
        b = a.copy()
        b = abs(b - v)
        b = b.apply(lambda x: sum([y for y in range(1, x+1)]))
        if (cost := b.sum()) < fuel_cost:
            fuel_cost = cost
    print(fuel_cost)
