import os
import sys


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = f.read().splitlines()

    h_pos, depth_pos = 0, 0
    for line in input_list:
        if line.startswith("f"):
            h_pos += int(line.split(" ")[1])
        elif line.startswith("d"):
            depth_pos += int(line.split(" ")[1])
        if line.startswith("u"):
            depth_pos -= int(line.split(" ")[1])
    result_1 = h_pos * depth_pos
    print(result_1)

    h_pos, depth_pos, aim = 0, 0, 0
    for line in input_list:
        if line.startswith("f"):
            h_pos += int(line.split(" ")[1])
            depth_pos += aim * int(line.split(" ")[1])
        elif line.startswith("d"):
            aim += int(line.split(" ")[1])
        if line.startswith("u"):
            aim -= int(line.split(" ")[1])
    result_2 = h_pos * depth_pos
    print(result_2)
