#Write a Python program that takes a user's input for the price of a Zomato order as a string,
#converts it to a float using type casting, adds 18% GST, and prints the final bill amount.

price = input("Enter zometo price: ")
price = float(price)
gst = price*0.18
total_price = price + gst

print(price)
print(gst)
print(total_price)