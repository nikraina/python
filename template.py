__author__ = 'nikhil'

from string import Template

cart = []
cart.append(dict(item="biscuit", price = 10, qty = 1))
cart.append(dict(item="cake", price = 20, qty = 3))
cart.append(dict(item="coffee", price = 2, qty = 2))

t = Template("$qty * $item = $price")

total = 0
print "Your Cart is ::"

for item in cart:
    print t.substitute(item)
    total += item["price"]

print "The total amount for cart is :: " + str(total)


