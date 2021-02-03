#! /usr/bin/env python3

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val == self.val:
            return
        if val < self.val:
            if self.left != None:
                self.left.insert(val)
            else:
                self.left = Node(val)
        elif val > self.val:
            if self.right != None:
                self.right.insert(val)
            else:
                self.right = Node(val)
    
    def preorder(self):
        if self.val:
            print(self.val)
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()

    def inorder(self):
        if self.left != None:
            self.left.inorder()
        if self.val:
            print(self.val)
        if self.right != None:
            self.right.inorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        if self.val:
            print(self.val)

class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.root.insert(val)
    
    def inorder(self):
        self.root.inorder()

def test():
    t = Tree()
    for i in 50, 10, 60, 20, 70, 30, 80:
        t.insert(i)
    
    t.inorder()

test()
