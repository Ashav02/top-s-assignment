#Prodcut name clean 

product_name = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

name = []

for product in product_name:
    product = product.strip()
    product = product.replace("-", " ")
    product = product.title()

    name.append(product)

print(name)    

