#!/usr/bin/env python3

import sys, random

if len(sys.argv) < 2:
    print("missing input file")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()
    f.close()

words = content.split()
random.shuffle(words)
print(" ".join(words))