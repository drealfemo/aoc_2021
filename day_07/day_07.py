import os
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = list(map(int, [x.split(",") for x in f.read().splitlines()][0]))
    possible_pos = [x for x in range(min(*input_list), int(max(*input_list)/2))]

    # part one
    fuel_cost = 9999999999999
    for v in possible_pos:
        b = sum([abs(x-v) for x in input_list])
        if (cost := b) < fuel_cost:
            fuel_cost = cost
    print(fuel_cost)

    # part two
    fuel_cost = 9999999999999
    for v in possible_pos:
        b = [abs(x - v) for x in input_list]
        c = sum([sum([y for y in range(1, x+1)]) for x in b])
        if (cost := c) < fuel_cost:
            fuel_cost = cost
    print(fuel_cost)
