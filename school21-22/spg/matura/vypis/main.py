#!/usr/bin/env python

from typing import List


def vypis(file: str, width: int, do: bool = True, word: str = '') -> None:
    lines: List[str] = list()
    with open(file, "r") as fp:
        [lines.append(" ".join(line.strip().split()))
            for line in fp.readlines()]
        fp.close()
    paragraphs: List[str] = list()
    buffer = ""
    for line in lines:
        if line:
            if buffer:
                buffer = f"{buffer} {line}"
            else:
                buffer = line
        if not line:
            if buffer:
                paragraphs.append(buffer)
                buffer = ""
            else:
                continue

    paragraphs.append(buffer)
    input = list()

    if word:
        for paragraph in paragraphs:
            l = [word for word in paragraph.split()]
            if word in l:
                input.append(paragraph)
    else:
        input = paragraphs

    for paragraph in input:
        if len(paragraph) == width:
            print(f"{paragraph}")
            print()
        if len(paragraph) > width:
            words = [word for word in paragraph.split(" ")]
            lens = [len(word) for word in words]
            sum = 0
            index = 0
            for l in lens:
                if sum + l == width:
                    index += 1
                    line_words = [words.pop(0) for _ in range(index) ]
                    line = ""
                    for ii, word in enumerate(line_words):
                        if ii == 0:
                            line = word
                        else:
                            line += f" {word}"
                    sum = 0
                    index = 1
                    print(f"{line}")
                elif sum + l > width:
                    sum -= 1
                    line_words = [words.pop(0) for _ in range(index) ]
                    given_spaces = len(line_words) - 1
                    spaces = width - sum
                    line = ""
                    num_spaces = []
                    gs = given_spaces
                    if do:
                        for ii in range(gs):
                            n = spaces // given_spaces
                            num_spaces.append(n)
                            spaces -= n
                            given_spaces -= 1
                        num_spaces.reverse()
                        for ii, word in enumerate(line_words):
                            if ii == 0:
                                line = word
                            else:
                                line += " " + " " * num_spaces.pop(0) + word
                    else:
                        for ii, word in enumerate(line_words):
                            if ii == 0:
                                line = word
                            else:
                                line += f" {word}"
                    print(f"{line}")
                    sum = 0
                    index = 0

                sum += l + 1
                index += 1

            if words:
                print(" ".join(words).strip())
            print()

        if len(paragraph) < width:
            print(f"{paragraph}")
            print()


vypis("input.txt", 20, True, "")
