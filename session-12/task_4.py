#Given a list of order amounts from a Zomato cart [120, 340, 560, 80],
#use reduce() from functools to calculate the total bill amount.

Zometo_cart = [120, 340, 560, 80]

import functools
from functools import reduce

final_bill_amt = reduce(lambda x, y: x + y, Zometo_cart)

print("Total Bill Amount : ",final_bill_amt)
