#Build a class called Playlist that has a private attribute _songs (a list of song names).
#Write methods to add a song, remove a song, and get the current list of songs using proper encapsulation.

#Class_1 (Prenet Class)

class Playlist:
    def __init__(self):
        self.song = []

    #add song
    def add_song(self, song):
        self.song.append(song)

    #remove song
    def remove_song(self, song):
        if song in self.song:
            self.song.remove(song)
        else:
            print("Song not fount")

    #Getter

    def get_songs(self):
        return self.song

#Object (Child Class)

playlist = Playlist()

playlist.add_song("Brown Rang")
playlist.add_song("Tum Hi Hoo")

print("songs:", playlist.get_songs())
        

        