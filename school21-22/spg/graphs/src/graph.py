#! /usr/bin/env python3

class Node:
    id = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours: list[Node] = []
        Node.id += 1
        self.id = Node.id

    def add(self, n):
        n.neighbours.append(self)
        self.neighbours.append(n)

    def remove(self, n):
        n.neighbours.remove(self)
        self.neighbours.remove(n)

    def clicked(self, x, y):
        if x - 20 < self.x <= x + 20 and y - 20 < self.y <= y + 20:
                return True
        return False

class Graph:
    def __init__(self):
        self.nodes = []
        self.selected = []

    def insert(self, x, y):
        self.nodes.append(Node(x, y))

    def connect(self, a, b):
        a.add(b)
    
    def remove(self, x, y): 
        for node in self.nodes:
            if node.clicked(x, y):
                for ne in node.neighbours:
                    node.remove(ne)
                self.nodes.remove(node) 

    def select(self, x, y):
        for node in self.nodes:
            if node.clicked(x, y):
                if node in self.selected:
                    self.selected.clear() 
                self.selected.append(node)

        if len(self.selected) == 2:
            self.connect(self.selected[0], self.selected[1])
            self.selected.clear()

    def draw(self, canvas):
        canvas.delete("all")
        for n in self.nodes:
            canvas.create_oval(n.x - 20, n.y - 20, n.x + 20, n.y + 20)
            canvas.create_text(n.x, n.y, text=n.id)
            for ne in n.neighbours:
                canvas.create_line(n.x, n.y, ne.x, ne.y)
