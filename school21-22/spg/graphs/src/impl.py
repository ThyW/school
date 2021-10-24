#!/usr/bin/env python3

from typing import List, NamedTuple, Tuple 
from heapq import heappush, heappop

class Pair(NamedTuple):
    node_a: int
    node_b: int
    weight: int

class Graph:
    INF: int = 100000
    def __init__(self) -> None:
        self.nodes: List[int] = []
        self.vertecies: List[Pair] = []

    def add_node(self, id: int) -> None:
        self.nodes.append(id)

    def add_vertex(self, node_a: int, node_b: int, weight: int) -> None:
        self.vertecies.append(Pair(node_a, node_b, weight))

    def spa(self, start: int, end: int) -> int:
        heap: List[Tuple[int, int]] = []
        heappush(heap, (start, 0))
        for each_node in self.nodes:
            if each_node != start:
                heappush(heap, (each_node, Graph.INF))

        while heap:
            v: Tuple[int, int] = heappop(heap)

        return 0
