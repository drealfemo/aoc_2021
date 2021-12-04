import os
import sys


def get_num_of_increments(input_l, window=1):
    input_l = [input_l[i: i+window] for i in range(len(input_l))]
    input_l = [x for x in input_l if len(x) == window]
    diffs = [sum(y) - sum(x) for x, y in zip(input_l, input_l[1:])]
    return len([x for x in diffs if x > 0])


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()
        input_list = [int(x) for x in input_list]
    result_1 = get_num_of_increments(input_list)  # part one
    print(result_1)
    result_2 = get_num_of_increments(input_list, window=3)  # part two
    print(result_2)
