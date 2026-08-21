#Define a Python class called Song with attributes title, artist, and duration (in seconds),
#and use the __init__() constructor to initialize these values when creating an object.

#Class 1 (Perent)
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artise = artist
        self.duration = duration


#Object
my_song = Song("Byte","Martin Garrix",285)
print(my_song.title, my_song.artise, my_song.duration)