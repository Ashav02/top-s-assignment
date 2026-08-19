#Define a Python class called Song with attributes title, artist, and duration (in seconds),
#and use the __init__() constructor to initialize these values when creating an object.

class song:
    def __init__(self, title, singer, length):
        self.title = title
        self.singer = singer
        self.length = length 

song1 = song("Naina Lagiya", "Mohit Chohan",263)


print(song1.title)
print(song1.singer)
print(song1.length)

