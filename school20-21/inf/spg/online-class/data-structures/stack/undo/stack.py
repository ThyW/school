#! /usr/bin/env python3 

from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: Optional[Node[T]] = None


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.top: Optional[Node[T]] = None

    def push(self, value: T) -> None:
        new = Node(value)
        if not self.top:
            self.top = new
        else:
            old = self.top
            self.top = new
            new.next = old
    
    def pop(self) -> Optional[Node[T]]:
        if not self.top: 
            return None
        else:
            new_top = self.top.next
            ret = self.top
            self.top = new_top
            return ret

    def __repr__(self) -> str:
        ret = ""
        current = self.top
        while current != None:
            ret = f"{ret}{current.value}\n"
            current = current.next
        return ret
    
    def clear(self) -> None:
        self.top = None
