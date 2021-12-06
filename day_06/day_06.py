import os
import sys
from collections import Counter


# def number_of_fish_after_period(initial_fish, number_of_days=80):
#     current_fish = initial_fish
#     add_new = False
#     new_count = 0
#     for day in range(number_of_days + 1):
#         if add_new:
#             current_fish = current_fish + [8] * new_count
#             add_new = False
#             new_count = 0
#         if day == number_of_days:
#             break
#         n = len(current_fish)
#         new_fish = [None] * n
#         for i, val in enumerate(current_fish):
#             new_val = val - 1
#             if new_val < 0:
#                 new_val = 6
#                 add_new = True
#                 new_count += 1
#             new_fish[i] = new_val
#         current_fish = new_fish
#     # print(current_fish)
#     return len(current_fish)


def number_of_fish_after_period(fish, days=80):
    fish = Counter(fish)
    for i in range(days):
        new_fish = fish[0]
        for i in range(8):
            fish[i] = fish[i + 1]
        fish[8] = new_fish
        fish[6] += new_fish
    return sum(fish.values())


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = [x.split(",") for x in f.read().splitlines()]
    input_list = [int(x) for x in input_list[0]]

    # part one
    print(number_of_fish_after_period(input_list))

    # part two
    print(number_of_fish_after_period(input_list, days=256))
