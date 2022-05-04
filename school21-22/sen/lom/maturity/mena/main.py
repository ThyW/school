#!/usr/bin/env python3

import string

with open("input", "r") as f:
    l = []
    for line in f.readlines():
        out = []
        for char in line.strip():
            if char in string.ascii_letters:
                out.append(char)
        name = "".join(out)
        name = name.lower()
        name = name.capitalize()
        l.append(name)
    print(l)
