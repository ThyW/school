#!/usr/bin/env python3

from typing import List

def merge_sort(input: List[int]) -> None:
    l = len(input)
    if not l > 1:
        return
    m = l//2

    f = input[m:]
    s = input[:m]

    merge_sort(f)
    merge_sort(s)

    a = b = c = 0

    while a < len(f) and b < len(s):
        if f[a] < s[b]:
            input[c] = f[a]
            a += 1
        else:
            input[c] = s[b]
            b += 1
        c += 1

    while a < len(f):
        input[c] = f[a]
        a += 1
        c += 1

    while b < len(s):
        input[c] = s[b]
        b += 1
        c += 1

a = [2, 7, 1, -6, 20, 33, -1]

merge_sort(a)
assert a == [-6, -1, 1, 2, 7, 20, 33]
print(a)
