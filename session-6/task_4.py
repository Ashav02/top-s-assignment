#Given two sets: set1 contains the names of restaurants you have ordered from on Zomato
#and set2 contains the names of restaurants you have ordered from on Swiggy, find 
#and print the union and intersection of these sets.

zometo_set1 = {'Jalaram Khichadi','La Pinoz Pizza','MacD','Wok on Fire'}
swiggy_set2 = {'Dominos', 'Wok on Fire','MacD','KFC'}


#Union 
Union = zometo_set1.union(swiggy_set2)
print(Union)

#Intersection 

Intersection = zometo_set1.intersection(swiggy_set2)
print(Intersection)