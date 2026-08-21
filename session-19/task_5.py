#Refactor your Song class so that it also tracks a play_count attribute (starting at 0),
#and add a method increment_play_count(self) that increases play_count by 1 each time it's called.
#Show how you would use this to count how many times a user plays a song. 
#Call increment_play_count() multiple times and print play_count to see the update.
class Song: 
    def __init__(self, track, singer, length):
        self.track = track
        self.singer = singer
        self.length = length
        self.play_count = 0

    def increment_play_count(self):
        self.play_count += 1

song_1 = Song("Blue Eyes", "Yo Yo Honey Singh", 242)

song_1.increment_play_count()
song_1.increment_play_count()
song_1.increment_play_count()

print(song_1.track)
print(song_1.singer)
print(song_1.play_count)
