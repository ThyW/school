#! /usr/bin/env python3
mp = [[1, 1, 0, 0, 1],
      [1, 0, 0, 1, 1],
      [1, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [1, 1, 1, 1, 0]]


def solve(mp, r, c):
    mp[r][c] = 2
    if c+1 < len(mp[r]) and mp[r][c+1] == 1:
        solve(mp, r, c+1)

    if c-1>=0 and mp[r][c-1] == 1:
        solve(mp, r, c-1)

    if r+1<len(mp) and mp[r+1][c] == 1:
        solve(mp, r+1, c)
    if r-1>=0 and mp[r-1][c] == 1:
        solve(mp, r-1, c)

def main(mp):
    counter = 0
    for x in range(len(mp)):
        for c in range(len(mp[x])):
            if mp[x][c] == 1:
                counter +=1
                solve(mp, x, c)

    return counter

print(main(mp))
