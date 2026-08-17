#Define a function called calculate_final_price(price, discount_rate)
#that returns the final price after applying the discount.
#Test it with price 1200 and discount_rate 0.15.

price = int(input("Final Price: "))

def cal_final_price(price):
    if price >= 2500:
        dis = (price*0.2)
        cal_final_price = price - dis 
        return cal_final_price
    elif price >= 1000:
        dis (price*0.15)
        cal_final_price = price - dis    
        return cal_final_price
    else:
        print("No Discount applicable")

            