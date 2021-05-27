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
                return self
            return self.right.find_parent(val)

        if val < self.val:
            if val == self.left.val:
                return self
            return self.left.find_parent(val)
    
    def find_min_parent(self):
        if self.left == None:
            return None
        if self.left.left == None:
            return self
        else: 
            return self.left.find_min_parent()

    def find_max_parent(self):
        if self.right == None:
            return None
        if self.right.right == None:
            return self
        else:
            return self.right.find_max_parent()
    
    def delete(self, val):
            parent=self.find_parent(val)
            if parent==None:
                print("bruh") 

            replacement=None
            if parent.left!=None:
                if parent.left.val==val:
                    if parent.left.right==None:
                        deleted=parent.left
                        parent.left=parent.left.left
                        return deleted
                    else:
                        minP=parent.left.right.find_min_parent()
                        if minP==None:
                            replacement=parent.left.right
                            parent.left.right=parent.left.right.right
                        else:
                            replacement=minP.left
                            minP.left=minP.left.right

                        replacement.left=parent.left.left
                        replacement.right=parent.left.right
                        deleted=parent.left
                        parent.left=replacement
                        return deleted

            if parent.right!=None:
                if parent.right.val==val:
                    if parent.right.left==None:
                        deleted=parent.right
                        parent.right=parent.right.right
                        return deleted
                    else:
                        maxp=parent.right.left.find_max_parent()
                        if maxp==None:
                            replacement=parent.right.left
                            parent.right.left=parent.right.left.left
                        else:
                            replacement=maxp.right
                            maxp.right=maxp.right.left

                        replacement.left=parent.right.right
                        replacement.right=parent.right.left
                        deleted=parent.right
                        parent.right=replacement
                        return deleted
                        print(deleted)


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

    
    def rec_draw(self, can, x, y):
        can.create_oval(x, y, x + 30, y + 30)
        can.create_text(x + 15, y + 15, text = str(self.val))

        if self.left != None:
            can.create_line(x + 15, y + 15, x - 50 + 15, y + 50 + 15)
            self.left.rec_draw(can, x - 50, y + 50)

        if self.right != None:
            can.create_line(x + 15, y + 15, x + 50 + 15, y + 50 + 15)
            self.right.rec_draw(can, x + 50, y + 50)
        

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
        if self.root==None:
            return
        elif self.root.val==val:
            if self.root.left!=None:
                maxP=self.root.left.find_max_parent()
                if maxP==None:
                    self.root.left.right=self.root.right
                    self.root=self.root.left
                else:
                    rep=maxP.right
                    maxP.right=maxP.right.left
                    rep.left=self.root.left
                    rep.right=self.root.right
                    self.root=rep

            elif self.root.right!=None:
                minP=self.root.right.find_min_parent()
                if minP==None:
                    self.root.right.left=self.root.left
                    self.root=self.root.right
                else:
                    rep=minP.left
                    minP.left=minP.left.right
                    rep.left=self.root.left
                    rep.right=self.root.right
                    self.root=rep

        else:
            self.root.delete(val)

    def rec_draw(self, can, x, y):
        self.root.rec_draw(can, x, y)
        

def test():
    t = Tree()
    for i in 50, 10, 20, 30, 40, 70, 100:
        t.insert(i)

test()
