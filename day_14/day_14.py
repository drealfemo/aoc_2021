import os
import sys
from math import ceil


def solver(steps=10):
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = f.read().splitlines()
        tmpl = lines[0]

        rules = {}
        for line in lines[2:]:
            pair, insertion = line.split(" -> ")
            rules[pair] = (pair[0] + insertion, insertion + pair[1])

    polymer = {}
    for i in range(len(tmpl) - 1):
        polymer[tmpl[i] + tmpl[i + 1]] = polymer.setdefault(tmpl[i] + tmpl[i + 1], 0) + 1

    for _ in range(steps):
        new_polymer = {}
        for p, val in polymer.items():
            for r in rules[p]:
                new_polymer[r] = new_polymer.setdefault(r, 0) + val

        polymer = new_polymer

    elements = {}
    for rule, amount in polymer.items():
        elements[rule[0]] = elements.setdefault(rule[0], 0) + amount
        elements[rule[1]] = elements.setdefault(rule[1], 0) + amount
    elements = sorted([ceil(val / 2) for val in elements.values()])
    return elements[-1] - elements[0]


if __name__ == '__main__':
    print(solver())  # part 1
    print(solver(40))  # part 2
