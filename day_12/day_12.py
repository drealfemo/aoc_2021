import os
import sys
from collections import defaultdict, Counter
import itertools


def flat2gen(a_list):
    for item in a_list:
        if isinstance(item, tuple) or isinstance(item, list):
            for sub_item in item:
                yield sub_item
        else:
            yield item


def find_routes(routes, small_cave_visits=1):
    step = 0
    res = []
    while step < 40:  # 40 is random (could use lack of change in res to know when to stop)
        new_r = []
        for ns in routes:
            x = itertools.product([ns], adj[ns[-1]])
            for y in x:
                y = list(flat2gen(y))
                lower_case = [e for e in y if e.islower()]
                if lower_case:
                    count = Counter(lower_case)
                    limit_exceeded = False
                    if small_cave_visits == 2:
                        twos = [e for e in count.values() if e == 2]
                        greater_than_two = any([e for e in count.values() if e > 2])
                        if len(twos) > 1 or greater_than_two:
                            limit_exceeded = True
                    else:
                        limit_exceeded = [e for e in count.values() if e > small_cave_visits]
                    if limit_exceeded:
                        continue
                if y.count("start") == 1 and y.count("end") == 1:
                    res.append(y)
                    continue
                elif y.count("start") > 1:
                    continue
                new_r.append(y)
        else:
            routes = new_r
        step += 1
    return len(res)


if __name__ == '__main__':
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        input_list = [x.split("-") for x in f.read().splitlines()]

    adj = defaultdict(set)
    for vx in input_list:
        for i, n in enumerate(vx):
            if n not in adj:
                adj[n].add(vx[i - 1])
            else:
                adj[n].add(vx[i - 1])

    init_routes = []
    for ns in adj["start"]:
        x = list(itertools.product(["start"], [ns]))
        for y in x:
            init_routes.append(y)

    print(find_routes(init_routes))  # part 1
    print(find_routes(init_routes, small_cave_visits=2))  # part 2
