#Create an object of the Song class for your favorite track from Spotify,
#and print out its title and artist using object attributes.

#Class 1 (Perent)
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        print(f"My Favorite Track on Spotify {self.title} Ft.{self.artist}.")

#Object
My_Fav = Song("Sach Keh Raha Hai Deewana","B Park")
    