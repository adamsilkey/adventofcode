# pylint: disable-all

import sys


def parse_input(filename):
    with open(filename) as f:
        dic = {}
        for line in f:
            l = line.strip().split()
            idx = l.pop(0)
            l.pop(0)
            l = ''.join(l)
            l = [int(i) for i in l.split(',')]
            dic[int(idx)] = l
        return dic

'''
def pipewalk(check_num, pipe_dict, pipe_list):
    for i in pipe_dict[check_num]:
        if i not in pipe_list:
            pipe_list.append(i)
            pipewalk(i, pipe_dict, pipe_list)
'''


def pipewalk(check_num, pipe_dict, pipe_list = None):
    if pipe_list is None:
        pipe_list = []
    for i in pipe_dict[check_num]:
        if i not in pipe_list:
            pipe_list.append(i)
            pipewalk(i, pipe_dict, pipe_list)

    return pipe_list


def solve(inp):

    pipegroups = []

    while inp:
        pipe = inp.popitem()
        inp[pipe[0]] = pipe[1]
        group = pipewalk(pipe[0], inp)
        for key in group:
            del inp[key]
        pipegroups.append(group)


    print(pipegroups)
    print(len(pipegroups))

    #pipewalk(0, inp, pipelist)



    print(pipelist)
    print(len(pipelist))
    return inp


#sys.exit()
solve(parse_input('input.txt'))

