#Use filter() and a lambda function to extract only those Flipkart product names from a list that start with the letter 'S' (case-insensitive).

flipkart_list = ['Shoes','shorts','T-shirt','slipper','flip-flop']

short_list = list(filter(lambda x:x.lower().startswith("s"),flipkart_list))
print(short_list)
