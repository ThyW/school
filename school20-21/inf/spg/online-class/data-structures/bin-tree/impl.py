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

    def find_parent(self, val):
        if self.val == val:
            return None
        
        if val > self.val:
            if val == self.right.val:
                return self.right
            return self.right.find_parent(val)

        if val < self.val:
            if val == self.left.val:
                return self.left
            return self.left.find_parent(val)
    
    def find_min_parent(self):
        if self.left == None:
            return None
        if self.left.left == None:
            return self
        
        return self.left.find_min_parent()

    def find_max_parent(self):
        if self.right == None:
            return None
        if self.right.right == None:
            return self
        else:
            return self.right.find_max_parent()
    
    def delete(self, val):
        if self.val == val:
            return None
        else:
            parent = self.find_parent(val)
            if parent.left != None:
                if parent.left.val == val:
                    if parent.left.right == None:
                        d = parent.left
                        parent.left = parent.left.left
                        return d
                    else:
                        min_p = parent.find_min_parent()
                        if min_p == None:
                            repl = parent.left.right
                            parent.left.right = parent.left.right.right
                        else:
                            repl = min_p.left
                            min_p.left = min_p.left.right

                        repl.left = parent.left.left
                        repl.right = parent.left.right
                        ret = parent.left
                        parent.left = repl
                        return ret

            if parent.right != None:
                if parent.right.val == val:
                    if parent.right.left == None:
                        d = parent.right
                        parent.right = parent.right.right
                        return d
                    else:
                        max_p = parent.find_max_parent()
                        if max_p == None:
                            repl = parent.right.left
                            parent.right.left = parent.right.left.left
                        else: 
                            repl = max_p.right
                            max_p.right = max_p.right.left

                        repl.right = parent.right.right
                        repl.left = parent.right.left
                        ret = parent.right
                        parent.right = repl
                        return ret

    def count(self):
        if self.left != None:
            return self.left.count() + 1
        if self.right != None:
            return self.right.count() + 1
        else:
            return 1

    def addition(self):
        if self.left != None:
            return self.left.addition() + self.val
        if self.right != None:
            return self.right.addition() + self.val
        else:
            return self.val



class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.root.insert(val)
    
    def inorder(self):
        print(self.root.inorder())

    def count(self):
        print(self.root.count())
    
    def addition(self):
        print(self.root.addition())
    def delete(self, val):
        if self.root == None:
            return
        self.root.delete(val)

def test():
    t = Tree()
    for i in 50, 10, 20, 30, 40, 70, 100:
        t.insert(i)
    
    t.inorder()
    print("")
    t.count()
    print("")
    t.addition()
    t.delete(20);

    t.inorder()
    print(t.root.val)

test()
