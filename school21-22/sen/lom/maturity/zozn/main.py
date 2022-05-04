#!/usr/bin/env python3

from typing import List

def flatten(input: List) -> List:
    out = []
    for each in input:
        if type(each).__name__ == "list":
            out.extend(flatten(each))
        else:
            out.append(each)
    return out

print(flatten([1, 2, ["hello", "world", [3, 4,], "dvere"], 19]))
