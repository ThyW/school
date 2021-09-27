#!/usr/bin/env python3

class Node:
    def __init__(self):
        self.children = dict()
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        node = self.root
        for letter in key.lower():
            if not letter in node.children.keys():
                node.children[letter] = Node()
            node = node.children.get(letter)
            if node.word_end == True: node.word_end = False
        node.word_end = True

    def serach(self, key):
        node = self.root
        for char in key:
            if char in node.children.keys():
                node = node.children[char]
            else:
                return False
        return node.word_end
    
def test():
    trie = Trie()

    trie.insert("dvere")
    trie.insert("dick")

test()
