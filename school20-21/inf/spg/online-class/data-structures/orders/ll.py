#! /usr/bin/env python3

class Node: 
    def __init__(self, id, name, amount) -> None:
        self.next = None
        self.id = id
        self.name = name 
        self.amount = amount


class LL:
    def __init__(self, id, name, amount) -> None:
        self.id = 1000
        self.head = Node(id, name, amount)
    
    def append(self, name, amount):
        n = Node(self.id, name, amount)
        self.id += 1
        cur = self.head 
        while cur.next != None:
            cur = cur.next
        cur.next = n

    def delete(self, id):
        if self.head.id == id: 
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next != None:
                if cur.next.id == id:
                    cur.next = cur.next.next
                    return
                else:
                    cur = cur.next
    def __iter__(self):
        return ListIter(self)

class ListIter:
    def __init__(self, node) -> None:
        self.node = node.head
        self.c = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.node.next is None:
            raise StopIteration
        else:
            if self.c == 0:
                self.c += 1
                return self.node
            self.node = self.node.next
            return self.node
