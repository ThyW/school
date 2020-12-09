#! /usr/bin/env python3

import item
import user
import order

i1 = item.Item("jozko", 20.9)

o = order.Order()
o.add_item_i(i1, 3)
o.add_item("vodka", 14.88, 10)
o.add_item("bromhexin", 420.69, 200)

o2 = order.Order()
o2.add_item("Buzirky", 0.5, 10)
o2.add_item("pizza najlepisa owo uwu mna mnam dlhe meno haha", 10.70, 2)

u = user.User("jozko")
u.add_order(o)
u.add_order(o2)
u.list_orders()
u.show_orders()
