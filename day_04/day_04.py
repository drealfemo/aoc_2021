import os
import sys
from collections import Counter


def find_completed_board(b_scores, num_cols=5):
    for p, brd in enumerate(b_scores):
        x, y = Counter([a[0] for a in brd]), Counter([a[1] for a in brd])
        for m, n in zip(x.values(), y.values()):
            if m == num_cols or n == num_cols:
                return p
    return 999


def find_completed_boards(b_scores, num_cols=5):
    brds = []
    for p, brd in enumerate(b_scores):
        x, y = Counter([a[0] for a in brd]), Counter([a[1] for a in brd])
        for m, n in zip(x.values(), y.values()):
            if m == num_cols or n == num_cols:
                brds.append(p)

    if brds:
        return brds
    return 999


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().split("\n\n")
    numbers_order = input_list[0].split(',')
    boards = [x.splitlines() for x in input_list[1:]]
    boards = [[y.split() for y in x] for x in boards]

    # part one
    boards_scores = [[] for _ in boards]
    col_num = len(boards[0][0])
    winning_board_pos = None
    for i, num in enumerate(numbers_order):
        for j, board in enumerate(boards):
            for k, row in enumerate(board):
                for l, val in enumerate(row):
                    if num == val:
                        boards_scores[j].append([k, l])
                        if i >= col_num-1:
                            b = find_completed_board(boards_scores, num_cols=col_num)
                            if b != 999:
                                winning_board_pos = b
                                break
                if winning_board_pos:
                    break
            if winning_board_pos:
                break
        if winning_board_pos:
            break

    marked_pos = boards_scores[winning_board_pos]
    marked_values = []
    for mkd_p in marked_pos:
        marked_values.append(boards[winning_board_pos][mkd_p[0]][mkd_p[1]])

    winning_board = [y for x in boards[winning_board_pos] for y in x]
    for mkd_v in marked_values:
        winning_board.remove(mkd_v)

    result_1 = sum(int(x) for x in winning_board) * int(num)
    print(result_1)

    # part two
    boards_scores = [[] for _ in boards]
    winning_boards_order = []
    for i, num in enumerate(numbers_order):
        for j, board in enumerate(boards):
            for k, row in enumerate(board):
                for l, val in enumerate(row):
                    if num == val:
                        boards_scores[j].append([k, l])
                        if i >= col_num-1:
                            b = find_completed_boards(boards_scores, num_cols=col_num)
                            if b != 999:
                                for u in b:
                                    if u not in winning_boards_order:
                                        winning_boards_order.append(u)
        if len(winning_boards_order) == len(boards):
            break

    winning_board_pos = winning_boards_order[-1]
    marked_pos = boards_scores[winning_board_pos]
    marked_values = []
    for mkd_p in marked_pos:
        marked_values.append(boards[winning_board_pos][mkd_p[0]][mkd_p[1]])

    winning_board = [y for x in boards[winning_board_pos] for y in x]
    for mkd_v in marked_values:
        winning_board.remove(mkd_v)

    result_2 = sum(int(x) for x in winning_board) * int(num)
    print(result_2)
