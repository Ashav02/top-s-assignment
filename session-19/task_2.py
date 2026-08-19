#Create an object of the Song class for your favorite track from Spotify,
#and print out its title and artist using object attributes.

class song:
    def __init__(self, title, singer, length):
        self.title = title
        self.singer =singer
    

song2 = song("Tera Yaar Hoon Main", "Arijit Singh", 300)

print(song2.title)
print(song2.singer)

print("-------------")

song3 = song("High Heel", "Yo Yo Honey Singh", 250)

print(song3.title)
print(song3.singer)
