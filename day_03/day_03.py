import os
import sys
from collections import Counter


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = [list(x) for x in f.read().splitlines()]

    # part one
    all_bits = [[int(x[i]) for x in input_list] for i in range(len(input_list[0]))]
    gamma_rate = int("".join([str(max(x, key=x.count)) for x in all_bits]), 2)
    epsilon_rate = int("".join([str(min(x, key=x.count)) for x in all_bits]), 2)
    power_consumption = gamma_rate * epsilon_rate
    print(power_consumption)

    # part two
    max_list = input_list.copy()
    i = 0
    while len(max_list) != 1:
        current_bits_count = Counter([int(x[i]) for x in max_list])
        zero_count = current_bits_count[0]
        one_count = current_bits_count[1]
        if (one_count > zero_count) or (one_count == zero_count):
            max_list = [x for x in max_list if x[i] == "1"]
        elif one_count < zero_count:
            max_list = [x for x in max_list if x[i] == "0"]
        i += 1

    min_list = input_list.copy()
    i = 0
    while len(min_list) != 1:
        current_bits_count = Counter([int(x[i]) for x in min_list])
        zero_count = current_bits_count[0]
        one_count = current_bits_count[1]
        if (one_count > zero_count) or (one_count == zero_count):
            min_list = [x for x in min_list if x[i] == "0"]
        elif one_count < zero_count:
            min_list = [x for x in min_list if x[i] == "1"]
        i += 1

    oxygen_generator_rating = int("".join(max_list[0]), 2)
    co2_scrubber_rating = int("".join(min_list[0]), 2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print(life_support_rating)


