#! /usr/bin/env python3

import random
import item
import order

class User:
    used_ids = []
    def __init__(self, name):
        self.name = name
        id = random.randint(10000, 99999)
        while id in User.used_ids:
            id = random.randint(10000, 99999)
        self.id = id
        User.used_ids.append(self.id)
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
    
    def remove_order(self, id):
        for order in self.orders:
            if order.id == id:
                self.orders.remove(order)

    def list_orders(self):
        delim = str(9*"-" + 8*"-")
        print(delim)
        for i in range(len(self.orders)):
            if i == 0:
                line = str("| " + str(self.id) + " | " + str(self.orders[0].id) + " |")
                print(line)
            else:
                line = str("| " + "     " + " | " + str(self.orders[i].id) + " |")
                print(line)
        print(delim)

    def show_orders(self):
        for order in self.orders:
            print("USER: " + str(self.id))
            order.print_order()

