#Given two scenarios

fav_genres = ['Si-Fy','Drama','Horror','Advantur']

fav_genres.append('Action')
print(fav_genres)

fav_genres.remove('Horror')
print(fav_genres)

#favorite_genres is a list. And list is mutable.

IRCTC_train_classes = ('Sleeper', 'AC 3 Tier', 'AC 2 Tier')

IRCTC_train_classes[0] = "First Class"
print(IRCTC_train_classes)

#TypeError: 'tuple' object does not support item assignment
#Tuples is unmutable.