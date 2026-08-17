#Simulate a Flipkart cart with a list of item prices [299, 499, 199, 999, 149].
#Use a for loop and the continue statement to skip any item priced below 200,
#and print the total of the remaining items.

item_prices = [299, 499, 199, 999, 149]

total = 0

for price in item_prices:
    if price < 200:
        continue

    total += price 

    print("Total: ",total)