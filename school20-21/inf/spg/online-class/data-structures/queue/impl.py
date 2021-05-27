#! /usr/bin/env python3

from typing import TypeVar, Generic, Optional

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, val: T) -> None:
        self.val: T = val
        self.next: Optional[Node[T]] = None

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]]= None
        self.tail: Optional[Node[T]]= None

    def enqueue(self, val: T):
        new = Node(val)
        if self.head == None and self.tail == None:
            self.head = new
            self.tail = new
        
        else:
            self.tail.next = new
            self.tail = self.tail.next

    def dequeue(self) -> Optional[Node[T]]:
        if self.head == None:
            return None
        if self.head == self.tail:
            ret = self.head
            self.head = None
            self.tail = None
            return ret
        else:
            ret = self.head
            self.head = self.head.next
            return ret
    
    def __repr__(self) -> str:
        ret = ""
        current = self.head
        
        while current != None:
            ret = f"{ret}{current.val}\n"
            current = current.next
        return ret

def test():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    
    print(str(q))

    print([q.dequeue().val for x in range(5)])
