#Define a function called calculate_final_price(price, discount_rate)
#that returns the final price after applying the discount.
#Test it with price 1200 and discount_rate 0.15.

def calculate_final_price(price, dis_rate):
    dis = price * dis_rate
    final_price = price - dis
    return final_price

price = 1200
dis_rate = .15

final_price = calculate_final_price(price, dis_rate)

print("Enter final amount : ",final_price)
            