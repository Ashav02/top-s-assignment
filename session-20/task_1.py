#Create a Python class called Product with a private attribute _price.
#Initialize _price in the constructor and write a method to display its value.

#Class 1 

class Product:
    def __init__(self, price):
        self.price = price

    def display_price(self):
        print("Prodcut Price: ",self.price)

#Object

product = Product(50000)
product.display_price()