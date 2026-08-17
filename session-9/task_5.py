#Write a function called calculate_cashback(amount, cashback_rate=0.05) that returns the cashback amount.
#Then, use it to calculate cashback for a Zomato order of Rs. 500 with the default rate,
#and for a Flipkart order of Rs. 2000 with a 7% cashback.

def calculate_cashback(amount,cashback_rate=0.05):
    cashback = amount*cashback_rate
    return cashback

#Zometo Order : def. cashback 5%

zometo_cashback =calculate_cashback(500)
print("Zometo Cashback:",zometo_cashback)


#Flipart : def. cashback 5%

flipkart_cashback = calculate_cashback(2000,0.07)
print("flipkart:",flipkart_cashback)