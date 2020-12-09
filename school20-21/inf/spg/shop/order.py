#! /usr/bin/env python3
import random
import item

class Order:
    used_ids = []
    def __init__(self):
        id = random.randint(10000, 99999)
        while id in Order.used_ids:
            id = random.randint(10000, 99999)
        self.id = id
        Order.used_ids.append(self.id)
        self.items = []
    
    def add_item(self, name, price, number_of):
        it = item.Item(name, price)
        for i in range(number_of):
            self.items.append((it, number_of))

    def add_item_i(self, it, number_of):
        for i in range(number_of):
            self.items.append((it, number_of))
    
    def remove_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)

    def print_order(self):
        largest_order_name = 0
        for item in self.items:
            if len(item[0].name) > largest_order_name:
                largest_order_name = len(item[0].name)
            else:
                continue

        largest_order_number = 0
        for item in self.items:
            if item[1] > largest_order_number:
                largest_order_number = item[1]
        largest_order_number = len(str(largest_order_number))

        usable_items = []
        for item in self.items:
            if item[0] in usable_items:
                continue
            else:
                usable_items.append(item[0])

        amount = {}
        for item in self.items:
            if item[0].name in amount:
                amount[item[0].name] += 1
            else: 
                amount[item[0].name] = 1

        largest_price = 0
        for item in self.items:
            if len(str(item[0].price)) > largest_price:
                largest_price = str(item[0].price).__len__()
            else:
                continue

        lines = []
        for i in range(0, len(usable_items)):
            if i == 0:
                line1 = str("| " + str(self.id) + " | " + str(usable_items[0].name) + (largest_order_name-len(usable_items[0].name))*" " + " | " + str(usable_items[0].price) + (largest_price - len(str(usable_items[0].price)))*" " + " | " + str(amount[usable_items[0].name]) + (largest_order_number - len(str(amount[usable_items[0].name])))*" " + " |")
                lines.append(line1)
            else:
                line = str("| " + "     " + " | " + str(usable_items[i].name) + (largest_order_name - len(usable_items[i].name))*" "+ " | " + str(usable_items[i].price) + (largest_price - len(str(usable_items[i].price)))*" " + " | " + str(amount[usable_items[i].name]) + (largest_order_number - len(str(amount[usable_items[i].name])))*" " + " |")
                lines.append(line)

        delim = str(9*"-" + largest_order_name*"-" + "---" + largest_price*"-" + "---" + largest_order_number*"-" + "---")
        print(delim)
        for line in lines:
            print(line)
        print(delim)
        total = 0
        for i in range(len(usable_items)):
            total += amount[usable_items[i].name] * usable_items[i].price
        total = str("TOTAL: " + str(total))
        print(str((len(delim) - len(total))*" " + total))
