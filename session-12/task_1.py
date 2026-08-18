#Write a lambda function that takes a price in rupees and returns the price after adding 18% GST.
#Test it on the prices 100, 250, and 500.

add_gst = lambda price: price + (price * 0.18)

price=100
print(f"Price after GST {price} is: {add_gst(price)}")

price= 250
print(f"Price after GST {price} is: {add_gst(price)}")

price = 500
print(f"Price after GST {price} is : {add_gst(price)}")
