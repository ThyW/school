#/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.last = self.head

    def push_last(self, data):
        node = Node(data)
        node.prev = self.last
        node.next = None
        if self.last:
            self.last.next = node
            self.last = self.last.next

    def pop_last(self):
        if self.last:
            temp = self.last
            self.last = self.last.prev
            self.last.next = None
            return temp.data
    
    def push_first(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def pop_first(self, data):
        if self.head:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            return temp.data

    def get(self, data):
        node = self.head
        while node:
            if node.data == data:
                return data
            node = node.next
        return None
