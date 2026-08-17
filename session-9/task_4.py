#Given a function apply_discount(price, rate=0.10),
#update it so that if the rate is not passed, it uses 0.10 by default.
#Then, call it with only the price argument and print the result.

def apply_discount(price, rate=0.10):
    dis = price*0.10
    final_price = price - dis
    return final_price

price = 10000

print(apply_discount(price))