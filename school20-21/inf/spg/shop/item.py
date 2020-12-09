#! /usr/bin/env python3
import random

class Item:
    used_ids = []

    def __init__(self, name,  price):
        self.name = name
        self.price = price
        id = random.randint(10000, 99999)
        while id in Item.used_ids:
            id = random.randint(10000, 99999)
        self.id = id
        Item.used_ids.append(self.id)
