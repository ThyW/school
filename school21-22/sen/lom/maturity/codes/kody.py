#!/usr/bin/env python3
from typing import List


# third part
def cypher(input: List[str]) -> None:
    print("\n")
    i = [list(x) for x in input]
    while i:
        out = ""
        if any(i):
            for each in i:
                if each:
                    out += each[0]
                    each.pop(0)
            print(f"{out} ", end="")
        else:
            print(end= "\n")
            break


def main() -> None:
    words = []
    # first part
    with open("input.txt", "r") as file:
        for line in file.readlines():
            for word in line.split(" "):
                words.append(word.strip())
                # second part
                print(f"{len(word)} ", end="")

    file.close()
    cypher(words)


main()
