#Given two scenarios

favorite_genres = ['Si-Fy','Drama','Horror','Advantur']

favorite_genres.append('Action')
print(favorite_genres)

favorite_genres.remove('Horror')
print(favorite_genres)

#favorite_genres is a list. And list is mutable.

IRCTC_train_classes = ('Sleeper', 'AC 3 Tier', 'AC 2 Tier')

IRCTC_train_classes[0] = "First Class"
print(IRCTC_train_classes)

#TypeError: 'tuple' object does not support item assignment
#Tuples is unmutable.