#Build a Flipkart-style order summary: ask the user for item price and quantity,then calculate and print total price.
#Use try-except-else-finally blocks to handle ValueError for invalid input, print the total if successful, and always print 'Thank you for shopping!' in the finally block.

try: 
    item_price = float(input("Enter item price: "))
    qty = int(input("Enter item qty: "))

except ValueError:
    print("Error: Please enter valid number.")

else: 
    total_price = item_price * qty
    print("Total Price: ",total_price)

finally:
    print("Thank You, Visit again")