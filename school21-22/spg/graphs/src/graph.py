#! /usr/bin/env python3

from typing import NamedTuple, Optional, Tuple, List
from tkinter import Canvas
from heapq import heappush, heappop

class Pair(NamedTuple):
    id: int
    w: int
    def __gt__(self, x: "Pair") -> bool:
        return self.w > x.w

    def __lt__(self, x: "Pair") -> bool:
        return self.w < x.w
    
    def __eq__(self, x: "Pair") -> bool:
        return self.w == x.w

    def __ge__(self, x: "Pair") -> bool:
        return self.w >= x.w
    
    def __le__(self, x: "Pair") -> bool:
        return self.w <= x.w


class Node:
    id: int = 0

    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y
        self.neighbours: List[Tuple[Node, int]] = []
        Node.id += 1
        self.id: int = Node.id
        self.weight = 1000
        self.previous: Optional[Node] = None

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

    def __lt__(self, other: "Node"):
        return self.weight < other.weight


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

    def djikstra(self, start_id: int, finish_id: int, canvas: Canvas) -> None:
        heap = []
        end = None
        for each in self.nodes:
            each.previous = None
            if each.id == start_id:
                each.weight = 0
                print(each.id)
            if each.id == finish_id:
                print(each.id)
                end = each
            heappush(heap, each)

        while heap:
            for node_tuple in heap[0].neighbours:
                if node_tuple[0].weight > node_tuple[1] + heap[0].weight:
                    node_tuple[0].weight = node_tuple[1] + heap[0].weight
                    node_tuple[0].previous = heap[0]
            heappop(heap)
        
        print(end.weight)
        self.draw_path(finish_id, canvas)

    def draw_path(self, end: int, canvas: Canvas) -> None:
        self.draw(canvas)
        node = list(filter(lambda x: x.id == end, self.nodes))[0]

        while node.previous:
            canvas.create_line(node.x, node.y, node.previous.x, node.previous.y, fill="blue")
            node = node.previous
    def prim(self, start: int, canvas) -> None:
        heap = []
        for node in self.nodes:
            if node.id == start:
                node.weight = 0
            node.previous = None
        [heappush(heap, x) for x in self.nodes]
        visited = []
        while heap:
            for pair in heap[0].neighbours:
                if pair[0].weight > pair[1]:
                    pair[0].weight = pair[1]
                    pair[0].previous = heap[0]
            visited.append(heappop(heap))
        self.draw_prim(canvas)
    
    def draw_prim(self, canvas: Canvas) -> None:
        self.draw(canvas)
        for node in self.nodes:
            if node.previous:
                canvas.create_line(node.x, node.y, node.previous.x, node.previous.y, fill="green", width=3)
