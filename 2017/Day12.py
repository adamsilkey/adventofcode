# pylint: disable-all

from collections import deque

def parse_input(filename):
    with open(filename) as f:
        dic = {}
        for line in f:
            l = deque(line.replace(',', '').strip().split())
            idx = l.popleft()
            l.popleft()
            dic[int(idx)] = [int(i) for i in l]
        return dic

def pipewalk(check_num, pipe_dict, pipe_list = None):
    if pipe_list is None:
        pipe_list = []
    for i in pipe_dict[check_num]:
        if i not in pipe_list:
            pipe_list.append(i)
            pipewalk(i, pipe_dict, pipe_list)

    return pipe_list

def solve(pipe_dict):

    part_one = len(pipewalk(0, pipe_dict))

    pipegroups = []
    while pipe_dict:
        pipe = pipe_dict.popitem()
        pipe_dict[pipe[0]] = pipe[1]
        group = pipewalk(pipe[0], pipe_dict)
        for key in group:
            del pipe_dict[key]
        pipegroups.append(group)

    return part_one, len(pipegroups)

print(solve(parse_input('input.txt')))
