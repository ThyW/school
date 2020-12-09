#! /usr/bin/env python3

puzzle = [5, 4, 3, 2, 1, 3, 4, 3, 0]
visited = []

for i in range(len(pole)):
    visited.append(False)


def search(pole, vs, index):
    if pole[index] == 0:
        vs[index] = True
        print("Success")
        return

    vs[index] = True
    if index - pole[index] > 0:
        if vs[index+pole[index]] == False:
            search(pole, vs, index - pole[index])

    if index + pole[index] < len(pole):
        if vs[index + pole[index]] == False:
            search(pole, vs, index + pole[index])

search(puzzle, visited, 0)
print(visited)
if visited[-1]:
    print("pole has no solution")

else: 
    print("No solution")
