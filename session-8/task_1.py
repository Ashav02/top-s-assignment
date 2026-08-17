#Create a Python list called order_amounts with the values [120, 250, 90, 310, 150].
#Use a for loop to calculate and print the total order value.

order_amounts = [ 120, 250, 90, 310, 150 ]

total_order_value = 0

for amount in order_amounts:
    total_order_value +=amount

print(total_order_value)