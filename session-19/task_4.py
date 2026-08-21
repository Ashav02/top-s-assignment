#FoodOrder with attributes restaurant_name, items (a list), and total_price.
#Add a method add_item(self, item, price) that adds the item to the items list and updates total_price.
#Demonstrate by creating a FoodOrder object and adding two items like you would on Zomato.

#Class_1 (Perent)

class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price

my_order = FoodOrder("Benne By KP")

my_order.add_item("Benne Masala Dosa",250)


print(f"Restaurant Name: {my_order.restaurant_name}\n (items: {my_order.items})\n Total_Price: {my_order.total_price}")

    
