#! /usr/bin/env python3

from typing import NamedTuple, Optional, Tuple, List, Dict
from tkinter import Canvas
from heapq import heapify, heappush, heappop

class Pair(NamedTuple):
    id: int
    w: int
    def __gt__(self, x: Tuple[_T_co, ...]) -> bool:
        return super().__gt__(x)

class Node:
    id: int = 0

    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y
        self.neighbours: List[Tuple[Node, int]] = []
        Node.id += 1
        self.id: int = Node.id
        self.weight = 1000

    def add(self, n: "Node", w: int):
        n.neighbours.append((self, w))
        self.neighbours.append((n, w))

    def rem(self, n: Tuple["Node", int]):
        for i in range(len(n[0].neighbours)):
            if n[0].neighbours[i][0].id == self.id:
                del n[0].neighbours[i]
        for i in range(len(self.neighbours)):
            if self.neighbours[i][0] == n[0].id:
                del self.neighbours[i]

    def clicked(self, x: int, y: int) -> bool:
        if x - 20 < self.x <= x + 20 and y - 20 < self.y <= y + 20:
            return True
        return False


class Graph:
    def __init__(self):
        self.nodes: List[Node] = []
        self.selected: List[Node] = []

    def insert(self, x: int, y: int):
        self.nodes.append(Node(x, y))

    def connect(self, a: Node, b: Node, w: int):
        a.add(b, w)

    def remove(self, x: int, y):
        for node in self.nodes:
            if node.clicked(x, y):
                for ne in node.neighbours:
                    node.rem(ne)
                self.nodes.remove(node)

    def select(self, x: int, y: int, w: int = 1):
        for node in self.nodes:
            if node.clicked(x, y):
                if node in self.selected:
                    self.selected.clear()
                self.selected.append(node)

        if len(self.selected) == 2:
            self.connect(self.selected[0], self.selected[1], w)
            self.selected.clear()

    def draw(self, canvas: Canvas):
        canvas.delete("all")
        for n in self.nodes:
            canvas.create_oval(n.x - 20, n.y - 20, n.x + 20, n.y + 20)
            canvas.create_text(n.x, n.y-10, text=n.id)
            canvas.create_text(n.x, n.y+3, text=n.weight)
            for ne in n.neighbours:
                canvas.create_line(n.x, n.y, ne[0].x, ne[0].y)
                canvas.create_text(
                        (n.x+ne[0].x)/2,
                        (n.y+ne[0].y)/2,
                        text=ne[1])

    def djikstra(self, start_id: int, finish_id: int) -> None:
        vertex_value: int = 100000 # start value of all unvisited nodes
        heap: List[] = []
        dist: Dict[int, int] = dict()
        for each_node in self.nodes:
            dist[each_node.id] = vertex_value
        dist[start_id] = 0
        start_node = [x for x in self.nodes if x.id == start_id]
        start_node = start_node[0]
        other_nodes = [x for x in self.nodes if x.id != start_id]
        path: List[int] = []

        for each_node in other_nodes:
            heappush(heap, (vertex_value, each_node.id))
        heappush(heap, (0, start_node.id))

        while heap:
            smallest = heappop(heap)
            neighbours = [n for n in smallest.neightbours]

            #      a - - - e
            #      |\      |
            #      | -d - - b
            #      |  /     |
            #      c - - - -f
            #
            # a -> f
            # a - c = 3
            # a - e = 10
            # a - d = 5
            # c - d = 4
            # c - f = 8
            # d - b = 13
            # b - e = 8
            # b - f = 1
            # 
            # a - c - f = 8
            # a - c - d - b - f = 8
            #
            #
            #
            #
            #
            #
