import os
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()
    signal_patterns = [[y for y in (x.split(" | ")[0]).split()] for x in input_list]
    displayed_values = [[y for y in (x.split(" | ")[1]).split()] for x in input_list]

    # part one
    unique_segment_counts = [2, 4, 3, 7]  # 1 4 7 8
    res = len([y for x in displayed_values for y in x if len(y) in unique_segment_counts])
    print(res)

    # part two
    displayed_total = 0
    for i, signal_p in enumerate(signal_patterns):
        one = next(x for x in signal_p if len(x) == 2)
        four = next(x for x in signal_p if len(x) == 4)
        seven = next(x for x in signal_p if len(x) == 3)
        eight = next(x for x in signal_p if len(x) == 7)

        three = next(x for x in signal_p if len(x) == 5 and set(one).issubset(x))
        six = next(x for x in signal_p if len(x) == 6 and len(set(x).intersection(one)) == 1)
        five = next(x for x in signal_p if len(x) == 5 and set(x).issubset(six))
        two = next(x for x in signal_p if len(x) == 5 and x not in (three, five))
        new_e = list(set(two) - set(three))
        nine = next(x for x in signal_p if len(x) == 6 and new_e[0] not in x)
        zero = next(x for x in signal_p if len(x) == 6 and x not in (six, nine))

        digit_strings = [zero, one, two, three, four, five, six, seven, eight, nine]
        numbers = [str(x) for x in range(10)]
        num_str_map = {''.join(sorted(list(k))): v for k, v in zip(digit_strings, numbers)}

        displayed_total += int(''.join([num_str_map[''.join(sorted(list(x)))] for x in displayed_values[i]]))

    print(displayed_total)
