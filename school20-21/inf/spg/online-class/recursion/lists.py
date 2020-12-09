#! /usr/bin/env python3 

inp = [1, 2 , 3, [4, 5, [6], [8, 9, [1], 10]], 10, ['r']]

out = []

def solve(l, i, out):
    for e in range(len(l)):
        if str(type(l[e])) == "<class 'list'>":
            solve(l[e], 0, out)
        else:
            out.append(l[e])

solve(inp, 0, out)
print(out)
