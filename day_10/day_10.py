import os
import sys


def calculate_auto_complete_score(auto_comp):
    auto_complete_map = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for val in auto_comp:
        score = 5 * score + auto_complete_map[val]
    return score


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    opening_symbols = ("(", "[", "{", "<")
    closing_symbols = (")", "]", "}", ">")
    symbols = {k: v for k, v in zip(opening_symbols, closing_symbols)}
    reverse_symbols = {k: v for k, v in zip(closing_symbols, opening_symbols)}
    error_scores = {k: v for k, v in zip(closing_symbols, (3, 57, 1197, 25137))}

    syntax_error_score = 0
    scores = []
    for i, line in enumerate(input_list):
        openings = []
        for char in line:
            if char in opening_symbols:
                openings.append(char)
            elif char in closing_symbols:
                if reverse_symbols[char] != openings[-1]:
                    syntax_error_score += error_scores[char]
                    break
                else:
                    openings = openings[0:-1]
        else:
            auto_complete = [symbols[x] for x in openings][::-1]
            auto_complete_score = calculate_auto_complete_score(auto_complete)
            scores.append(auto_complete_score)

    print(syntax_error_score)  # part 1

    scores.sort()
    middle_score = scores[len(scores) // 2]
    print(middle_score)  # part 2
