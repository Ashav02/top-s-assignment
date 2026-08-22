#Add getter and setter methods for the _price attribute in your Product class to safely access and update the price.
#Make sure the setter prevents setting a negative price.

#Class 1 (perent Class)
class Product:
    def __init__(self, price):
        self.price = price

    #getter
    def get_price(self):
        return self.price

    #setter
    def s_price(self, new_price):
        if new_price < 0:
            raise ValueError("Error:Price can't be nagitive")
        self.price = new_price

#object
product = Product(30000)
print("Currnt Price:", product.get_price())

product.s_price(45000)
print("Updated Price: ",product.get_price())