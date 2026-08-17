#Create a function get_delivery_charge(amount, city='Ahmedabad') that returns a delivery charge: Rs. 30 for Ahmedabad, Rs. 50 for other cities.
#Call it with and without the city argument to see both results.

def get_delivery_charge(amount, city='Ahmedabad'):
    if city == 'Ahmedabad':
        return 30
    else:
        return 50    

print("Ahmedabad:",get_delivery_charge(500))        
print("Surat:",get_delivery_charge(500,'Surat'))  